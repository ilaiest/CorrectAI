from abc import ABC, abstractmethod

class BaseProvider(ABC):
    @abstractmethod
    def correct(self, prompt):
        pass
