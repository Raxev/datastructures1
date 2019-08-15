from comparable import Comparable
from date import Date

class Person(Comparable):
    """
    This class is immutable and inherits from Comparable
    It uses composition by having a Date object for birthday
    Please code this using private instance variables.
    Each instance variable should have a getter, but no setters
    Code the compare method, and call the base class compare
    Code a __str__ method
    """

    def __init__(self, name, year, month, day):
        self.__name = name
        self.__birthday = Date(year, month, day)

    def get_name(self):
        return self.__name

    def get_birthday(self):
        return self.__birthday

    def compare(self, person):
        Comparable.compare(self)
        if self.get_birthday().compare(person.get_birthday()) > 0:
            return 1
        elif self.get_birthday().compare(person.get_birthday()) == 0:
            if self.get_name() > person.get_name():
                return 1
            elif self.get_name() < person.get_name():
                return -1
            else:
                return 0
        else:
            return -1

    def __str__(self):
        return "{} {}".format(self.__name, self.__birthday)

