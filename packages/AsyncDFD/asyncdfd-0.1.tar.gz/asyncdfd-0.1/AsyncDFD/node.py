import traceback
import functools
from typing import Iterable
import logging

import gevent
from gevent import sleep, spawn
from gevent.queue import Queue
from tenacity import (
    retry,
    retry_if_not_exception_type,
    stop_after_attempt,
    wait_exponential_jitter,
)

from .exceptions import NodeProcessingError
from .abstract_node import AbstractNode
from .node_transferable import NodeTransferable
from .decorator import *

logger = logging.getLogger(__name__)


class Node(AbstractNode, NodeTransferable):
    def __init__(
        self,
        proc_func,
        criteria=lambda src_node, data: True,
        worker_num=None,
        queue_size=None,
        no_output=False,
        is_data_iterable=False,
        timeout=None,
    ) -> None:
        super().__init__()
        self.timeout = timeout if timeout else None
        self.worker_num = (
            worker_num if worker_num else 100
        )
        self.queue_size = (
            queue_size if queue_size else 10
        )

        self.__name__ = proc_func.__name__
        self.src_queue = Queue(self.queue_size)

        # first decorator will first wrap, as the inner decorator
        self.get_decorators = []
        self.proc_decorators = []
        self.put_decorators = []

        self._proc_data = self._error_decorator(proc_func)
        self.criteria = criteria

        self.is_data_iterable = is_data_iterable
        self.no_output = no_output

        self.get_data_lock = gevent.lock.Semaphore(1)

        self.tasks = []  # store all worker tasks
        self.executing_data_queue = []

    def start(self):
        """
        Starts the node's processing loop.
        """
        self._validate_destinations()
        self._setup_decorators()
        self._spawn_workers()
        super().start()
        logger.info(f"Node {self.__name__} start, src_nodes: {self.src_nodes}, dst_nodes: {self.dst_nodes}")
        return self.tasks

    def end(self):
        """
        Signals the end of the pipeline by putting a stop flag in the source queue.
        """
        # Need to wait for drain, so not set is_start to False
        super().end()
        for _ in range(self.worker_num):
            self.src_queue.put(StopIteration())
        gevent.joinall(self.tasks)

    def put(self, data):
        self.src_queue.put(data)

    def set_destination(self, node):
        self.dst_nodes[node.__name__] = node
        node.src_nodes[self.__name__] = self

    def add_proc_decorator(self, decorator):
        self.proc_decorators.append(decorator)

    def add_get_decorator(self, decorator):
        self.get_decorators.append(decorator)

    def add_put_decorator(self, decorator):
        self.put_decorators.append(decorator)

    def _validate_destinations(self):
        if self.no_output:
            assert (
                len(self.dst_nodes) == 0
            ), f"Node {self.__name__} has output queues, but set as no_output"
        else:
            assert len(self.dst_nodes) > 0, f"Node {self.__name__} dst_node is empty"

    def _setup_decorators(self):
        self._rearrange_proc_decorator()
        for decorator in self.get_decorators:
            self._get_one_data = decorator(self._get_one_data)
        for decorator in self.proc_decorators:
            self._proc_data = decorator(self._proc_data)
        for decorator in self.put_decorators:
            self._put_data = decorator(self._put_data)

    def _rearrange_proc_decorator(self):
        new_decorators = []

        def set_bottom_decorator(decorator):
            # former decorator in the inner layer
            if decorator in self.proc_decorators:
                new_decorators.append(decorator)
                self.proc_decorators.remove(decorator)

        def set_top_decorator(decorator):
            # latter decorator in the outer layer
            if decorator in self.proc_decorators:
                new_decorators.remove(decorator)
                new_decorators.append(decorator)

        for decorator in self.proc_decorators:
            new_decorators.append(decorator)

        set_top_decorator(label_proc_decorator)
        set_top_decorator(skip_data_decorator)

        self.proc_decorators = new_decorators

    def _spawn_workers(self):
        for i in range(self.worker_num):
            task = spawn(self._func_wrapper, i)
            self.tasks.append(task)

        self.get_data_generator = self._get_data()
        self.is_start = True
        return self.tasks

    def _func_wrapper(self, task_id):
        """
        Wraps the processing function and handles concurrency.
        """
        logger.debug(f"Name: {self.__name__}, id: {task_id} start")
        while self.is_start:
            data = None
            try:
                if len(self.executing_data_queue) < self.worker_num:
                    with self.get_data_lock:
                        data = next(self.get_data_generator)
                    self.executing_data_queue.append(data)
                    try:
                        result = self._proc_data(data)
                        self._put_data(result)
                    finally:
                        self.executing_data_queue.remove(data)
            except StopIteration:
                logger.info(f"Node {self.__name__} No. {task_id} stop")
                break
            except Exception as e:
                if data:
                    logger.error(
                        f"Unexpected error in func_wrapper: {e}\n"
                        + f"Data: {data}\n"
                        + f"Node name: {self.__name__}\n"
                        + traceback.format_exc()
                    )
                else:
                    logger.error(
                        f"Unexpected error in func_wrapper: {e}\n"
                        + f"Not get data\n"
                        + f"Node name: {self.__name__}\n"
                        + traceback.format_exc()
                    )
            sleep(0)

    def _get_data(self):
        while self.is_start:
            data = self.src_queue.get()
            yield from self._get_one_data(data)

    def _get_one_data(self, data):
        if isinstance(data, StopIteration):
            raise StopIteration()
        if self.is_data_iterable:
            assert isinstance(
                data, Iterable
            ), f"Unpack decorator only supports single iterable data, current data:{data}"
            for d in data:
                yield d
        else:
            yield data

    def _put_data(self, data):
        """
        Puts data to the destination queue.
        """
        for node in self.dst_nodes.values():
            if node.criteria(self, data):
                node.put(data)

    def _error_decorator(self, func):
        @retry(
            stop=stop_after_attempt(5),
            wait=wait_exponential_jitter(max=10),
            retry=retry_if_not_exception_type(StopIteration),
        )
        @functools.wraps(func)
        def error_wrapper(data):
            try:
                result = func(data)
                return result
            except StopIteration:
                raise
            except BaseException as e:
                error_stack = traceback.format_exc()
                logger.error(
                    f"{self.__name__} error: {e}, current queue size: {self.src_queue.qsize()}"
                )
                logger.error(f"Error stack:\n{error_stack}")
                raise e

        @functools.wraps(func)
        def final_wrapper(data):
            try:
                return error_wrapper(data)
            except BaseException as e:
                error_stack = traceback.format_exc()
                return NodeProcessingError((data), self.__name__, e, error_stack)

        return final_wrapper
