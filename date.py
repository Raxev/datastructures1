from comparable import Comparable


class Date(Comparable):
    """
    This class is immutable and inherits from Comparable
    Please code this using private instance variables.
    Each instance variable should have a getter, but no setters
    Code the compare method, but do not call the base class compare
    Code a __str__ method
    """

    def __init__(self, year, month, day):
        self.__year = int(year)
        self.__month = int(month)
        self.__day = int(day)

    def get_day(self):
        return self.__day

    def get_month(self):
        return self.__month

    def get_year(self):
        return self.__year

    def compare(self, obj):
        if self.__year < obj.get_year():
            return -1
        elif self.__year > obj.get_year():
            return 1
        if self.__month < obj.get_month():
            return -1
        elif self.__month > obj.get_month():
            return 1
        if self.__day < obj.get_day():
            return -1
        elif self.__day > obj.get_day():
            return 1
        return 0

    def __str__(self):
        return "{}-{}-{}".format(self.__month, self.__day, self.__year)
