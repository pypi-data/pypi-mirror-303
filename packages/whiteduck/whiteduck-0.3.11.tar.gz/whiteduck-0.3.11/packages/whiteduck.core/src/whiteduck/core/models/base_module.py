from abc import ABC, abstractmethod


class BaseModule(ABC):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @abstractmethod
    def run(self):
        """
        Run the module's main functionality.
        This method should be implemented by all subclasses.
        """
        pass

    @classmethod
    @abstractmethod
    def get_name(cls):
        """
        Get the name of the module.
        This method should be implemented by all subclasses.
        """
        pass

    @classmethod
    @abstractmethod
    def get_description(cls):
        """
        Get the description of the module.
        This method should be implemented by all subclasses.
        """
        pass
