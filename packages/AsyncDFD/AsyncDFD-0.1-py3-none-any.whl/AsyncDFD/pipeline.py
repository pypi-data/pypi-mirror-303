import hashlib
import logging
import functools
import itertools
from typing import List, Iterable
from gevent.queue import Queue

from .node import Node
from .label import LabelData
from .decorator import label_proc_decorator
from .node_group import NodeGroup
from .node_transferable import NodeTransferable

logger = logging.getLogger(__name__)


class Pipeline(NodeGroup, NodeTransferable):
    def __init__(
        self,
        all_nodes: List[Node],
    ):
        super().__init__(all_nodes=all_nodes)
        self.head = all_nodes[0]
        self.tail = all_nodes[-1]
        self.heads = {self.head.__name__: self.head}
        self.tails = {self.tail.__name__: self.tail}

    def _connect_nodes(self):
        former = None
        for node in self.all_nodes.values():
            if former is None:
                former = node
                continue
            else:
                logger.info(f"connect {former.__name__} to {node.__name__}")
                former.set_destination(node)
                former = node

    def start(self):
        assert (
            len(self.heads) == 1
        ), f"Only one head node is allowed in the pipeline {self.__name__}"
        assert (
            len(self.tails) == 1
        ), f"Only one tail node is allowed in the pipeline {self.__name__}"
        return super().start()

    def put(self, data):
        self.head.put(data)

    def set_destination(self, dst_node: Node):
        self.tail.set_destination(dst_node)

    @property
    def criteria(self):
        return self.head.criteria


class LabelPipeline(Pipeline):
    """
    A pipeline that processes data in an iterable format.

    This pipeline extends the base `Pipeline` class and provides additional functionality for processing data in an iterable format.
    It supports putting data into the pipeline, starting the pipeline, and getting processed data from the pipeline.

    Attributes:
        over_data_points (Queue): A queue that buffers the processed data points, waiting for assembling.
        proc_data_task: An task that retrieves processed data from the `over_data_points` queue and assemble them

    """

    def __init__(self, all_nodes: List[Node]):
        super().__init__(all_nodes=all_nodes)
        self.label_functions = []
        for node in self.all_nodes.values():
            node.add_proc_decorator(label_proc_decorator)
        self.head.add_get_decorator(self._label_get_data_decorator)
        self.tail.add_put_decorator(self._unlabel_put_data_decorator)

    def set_label_function(self, label_function):
        assert callable(
            label_function
        ), f"The label function {label_function} is not callable"
        self.label_functions.append(label_function)

    def get_data_func_label(self, label_data, func):
        assert isinstance(
            label_data, LabelData
        ), f"The data {label_data} is not a LabelData"
        assert (
            func in self.label_functions
        ), f"The function {func} is not in the label functions"
        label = label_data.label[0][func.__qualname__]
        return label

    def _label_get_data_decorator(self, get_func):
        @functools.wraps(get_func)
        def _label_get_data_wrapper(data):
            ret_data = get_func(data)
            for d in ret_data:
                label = {}
                for label_function in self.label_functions:
                    label[label_function.__qualname__] = label_function(d, data)
                label = (label,)
                label_data = LabelData(d, label)
                yield label_data

        return _label_get_data_wrapper

    def _unlabel_put_data_decorator(self, put_func):
        @functools.wraps(put_func)
        def _unlabel_put_data_wrapper(label_data):
            assert isinstance(
                label_data, LabelData
            ), f"The data {label_data} is not a LabelData"
            put_func(label_data.data)

        return _unlabel_put_data_wrapper


def generate_label(data):
    return hashlib.md5(str(data).encode("utf-8")).hexdigest()


class IterablePipeline(LabelPipeline):
    class ProcessingTask:
        def __init__(self, data):
            assert isinstance(data, Iterable), f"The data {data} is not an iterable"
            self.index = 0
            self.over_results = {}
            self.original_data = data
            self._iter = itertools.tee(data, 1)[0]
            next(
                self._iter
            )  # if they are the same, it will not raise StopIteration, should be shortened
            self.is_generator_exhausted = False
            self.task_label = generate_label(self.original_data)

        def get_label(self, data: tuple):
            try:
                next(self._iter)
            except StopIteration:
                self.is_generator_exhausted = True
            finally:
                index = self.index
                self.index += 1
                self.over_results[index] = None
                return (self.task_label, index)

    def __init__(self, all_nodes: List[Node]):
        super().__init__(all_nodes=all_nodes)
        self.processing_tasks = {}
        self.head.add_get_decorator(self._iterable_get_data_decorator)
        self.tail.add_put_decorator(self._iterable_put_data_decorator)
        self.head.is_data_iterable = True
        self.set_label_function(self.get_label)

    def get_label(self, data_point, data_gen):
        task = self.processing_tasks[generate_label(data_gen)]
        label = task.get_label(data_point)
        return label

    def _iterable_get_data_decorator(self, get_func):
        @functools.wraps(get_func)
        def _iterable_get_data_wrapper(iter_data):
            new_tasks = self.ProcessingTask(iter_data)
            self.processing_tasks[new_tasks.task_label] = new_tasks
            ret = get_func(iter_data)
            return ret

        return _iterable_get_data_wrapper

    def _iterable_put_data_decorator(self, put_func):

        @functools.wraps(put_func)
        def _iterable_put_data_wrapper(label_data):
            assert isinstance(
                label_data, LabelData
            ), f"The data {label_data} is not a LabelData"
            content = label_data.data
            label = label_data.label
            label = self.get_data_func_label(label_data, self.get_label)

            # put data to the right place
            task = self.processing_tasks[label[0]]
            task.over_results[label[1]] = content

            # check if all results ready
            if task.is_generator_exhausted and all(
                over_results := [v is not None for v in task.over_results.values()]
            ):
                data = LabelData((task.original_data, over_results), label[0])
                put_func(data)

        return _iterable_put_data_wrapper


class OrderPipeline(LabelPipeline):
    MAX_IDX = 1_000_000  # Define a maximum value for the index

    def __init__(self, all_nodes: List[Node]):
        super().__init__(all_nodes=all_nodes)
        self.data_idx = 0
        self.idx_queue = Queue()
        self.set_label_function(self.order_index_label_func)
        self.output_dict = {}

    def order_index_label_func(self, data):
        self.data_idx = (self.data_idx + 1) % self.MAX_IDX  # Circular incremen
        self.idx_queue.put(self.data_idx)
        return self.data_idx

    def _order_put_data_decorator(self, put_func):
        @functools.wraps(put_func)
        def _order_put_data_wrapper(label_data):
            assert isinstance(
                label_data, LabelData
            ), f"The data {label_data} is not a LabelData"
            label = self.get_data_func_label(label_data, self.order_index_label_func)
            self.output_dict[label] = label_data

            while not self.idx_queue.empty():
                next_idx = self.idx_queue.queue[0]  # Non-destructive check
                if next_idx in self.output_dict:
                    self.idx_queue.get()  # Remove the item from the queue
                    put_func(self.output_dict.pop(next_idx))
                else:
                    break

        return _order_put_data_wrapper


class CyclePipeline(Pipeline):

    def __init__(self, all_nodes: List[Node], head_output=False):
        super().__init__(all_nodes=all_nodes)
        self.tail.set_destination(self.head)
        if head_output:
            self.tail = self.head
