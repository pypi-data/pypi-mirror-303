from abc import ABC, abstractmethod

class BaseTemplate(ABC):
    @abstractmethod
    def generate(self):
        raise NotImplementedError()