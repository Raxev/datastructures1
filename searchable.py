from abc import ABC, abstractmethod

class Searchable(ABC):
    """
    This class only has an abstract method: search
    The search method takes a function object and a search object
    It uses pass for its implementation
    """
    @abstractmethod  # is this correct?
    def search(self, obj_list, obj):
        pass
