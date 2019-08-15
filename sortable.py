from abc import ABC, abstractmethod

class Sortable(ABC):
    """
    This class only has an abstract method: sort
    The sort method takes a function object.
    It uses pass for its implementation
    """

    @abstractmethod
    def sort(self, obj_list):
        pass
