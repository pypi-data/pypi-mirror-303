import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class AbstractNode(ABC):
    def __init__(self):
        # different layer of nodes will have different serial number
        # inherited from the parent node group
        self.serial_number = []
        self.__name__ = self.__class__.__name__
        self.is_start = False
        self._src_nodes = {}
        self._dst_nodes = {}

    @property
    def src_nodes(self):
        return self._src_nodes

    @src_nodes.setter
    def src_nodes(self, value):
        self._src_nodes = value

    @property
    def dst_nodes(self):
        return self._dst_nodes

    @dst_nodes.setter
    def dst_nodes(self, value):
        self._dst_nodes = value

    def set_name(self, name):
        self.__name__ = name

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    @abstractmethod
    def start(self):
        self.is_start = True

    @abstractmethod
    def end(self):
        self.is_start = False
