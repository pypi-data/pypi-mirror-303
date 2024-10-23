import time
import threading
import functools
import logging
from collections import defaultdict
from gevent.lock import Semaphore
from datetime import timedelta
from tabulate import tabulate

logger = logging.getLogger(__name__)


class SingletonMeta(type):
    _instances = {}
    _locks = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._locks:
            cls._locks[cls] = Semaphore()
        with cls._locks[cls]:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Monitor(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.registered_analysers = []
        self.start_time = None

    def start(self):
        for analyser in self.registered_analysers:
            analyser.start()
        self.thread = threading.Thread(target=self.get_all_info)
        self.thread.start()
        self.start_time = time.time()

    def get_all_info(self):
        while True:
            time.sleep(15)
            total_time = time.time() - self.start_time
            readable_time = str(timedelta(seconds=total_time))
            logger.info("=" * 80 + f"\nTotal execution time: {readable_time}")
            for analyser in self.registered_analysers:
                string = analyser.report()
                logger.info("=" * 80 + "\n" + string)

    def register(self, *analysers):
        for analyser in analysers:
            assert isinstance(analyser, Analyser)
            self.registered_analysers.append(analyser)


class Analyser(metaclass=SingletonMeta):
    def __init__(self) -> None:
        pass

    def start(self):
        raise NotImplementedError("Subclasses should implement this method")

    def report(self) -> str:
        raise NotImplementedError("Subclasses should implement this method")


class PipelineAnalyser(Analyser):

    class FuncInfo:
        def __init__(self, func):
            self.func = func
            self.exec_count = 0
            self.exec_time = 0
            self.interval_exec_count = 0
            self.interval_exec_time = 0

    def __init__(self):
        self.node_group = None
        self.node_executing_count = {}
        self.func_info = {}
        self.func_lock = defaultdict(Semaphore)

    def start(self):
        from .node import Node

        def add_decorator(node_group):
            for node in node_group.all_nodes.values():
                if isinstance(node, Node):
                    self.func_info[node.__name__] = self.FuncInfo(node._proc_data)
                    node.add_proc_decorator(self.decorator)
                else:
                    add_decorator(node)

        add_decorator(self.node_group)

    def decorator(self, func):
        @functools.wraps(func)
        def exec_time_wrapper(*args, **kwargs):
            func_name = func.__name__
            func_info = self.func_info[func_name]

            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()

            exec_time = end_time - start_time
            with self.func_lock[func_name]:
                func_info.interval_exec_time += exec_time
                func_info.interval_exec_count += 1

            return result

        return exec_time_wrapper

    def register(self, node_group):
        self.node_group = node_group

    def report(self) -> str:
        from .node import Node

        table = []
        headers = [
            "Serial",
            "Name",
            "Wait",
            "Exec",
            "Speed",
            "Avg Speed",
        ]

        def add_infos(node_group, table):
            for node in node_group.all_nodes.values():
                if isinstance(node, Node) and node.is_start:
                    info = self.func_info[node.__name__]
                    with self.func_lock[node.__name__]:
                        interval_exec_count = info.interval_exec_count
                        info.exec_count += interval_exec_count
                        total_exec_count = info.exec_count

                        interval_exec_time = info.interval_exec_time
                        info.exec_time += interval_exec_time
                        total_exec_time = info.exec_time

                        info.interval_exec_count = 0
                        info.interval_exec_time = 0
                    table.append(
                        [
                            ".".join(map(str, node.serial_number)),
                            node.__name__,
                            f"{node.src_queue.qsize()}/{node.src_queue.maxsize}",
                            f"{len(node.executing_data_queue)}/{node.worker_num}",
                            (
                                f"{interval_exec_count}/{interval_exec_time:.2f}s, {interval_exec_count / interval_exec_time:.2f}/s"
                                if interval_exec_time > 0
                                else "N/A"
                            ),
                            (
                                f"{total_exec_count}/{total_exec_time:.2f}s, {total_exec_time / total_exec_count:.2f}/s"
                                if total_exec_count > 0
                                else "N/A"
                            ),
                        ]
                    )
                else:
                    add_infos(node, table)

        add_infos(self.node_group, table)

        string = "Pipeline Report"
        string += "\n" + tabulate(table, headers, tablefmt="grid")
        return string
