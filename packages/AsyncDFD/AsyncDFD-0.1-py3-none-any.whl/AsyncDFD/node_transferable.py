import logging
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class NodeTransferable(ABC):

    @abstractmethod
    def put(self, data):
        pass

    @abstractmethod
    def set_destination(self, node):
        pass
