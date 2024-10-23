import logging
from typing import List
from abc import ABC, abstractmethod

import gevent
from gevent import spawn
from .node import Node
from .abstract_node import AbstractNode

logger = logging.getLogger(__name__)


class NodeGroup(AbstractNode, ABC):
    def __init__(self, all_nodes: List[Node]):
        super().__init__()
        assert len(all_nodes) != 0, f"No node to compose the node group {self.__name__}"
        self.all_nodes = {node.__name__: node for node in all_nodes}
        self.heads: dict[Node] = {}
        self.tails: dict[Node] = {}
        self._connect_nodes()

    @abstractmethod
    def _connect_nodes(self):
        logger.error(
            f"Not implemented the self._connect_nodes method in {self.__name__}"
        )

    def start(self):
        assert len(self.heads) != 0, f"No head node in the node group {self.__name__}"
        assert len(self.tails) != 0, f"No tail node in the node group {self.__name__}"
        if self.serial_number is None:
            self.serial_number = [0]
        for i, node in enumerate(self.all_nodes.values()):
            node.set_serial_number(self.serial_number + [i])
            node.start()
        super().start()
        return

    def end(self):
        super().end()
        end_tasks = []
        for node in self.all_nodes.values():
            end_tasks.append(spawn(node.end))
        gevent.joinall(end_tasks)

    @property
    def src_nodes(self):
        src_nodes = {}
        for node in self.heads.values():
            src_nodes.update(node.src_nodes)
        return src_nodes

    @property
    def dst_nodes(self):
        dst_nodes = {}
        for node in self.tails.values():
            dst_nodes.update(node.dst_nodes)
        return dst_nodes
