import csv
from person import Person
from sortable import Sortable
from searchable import Searchable


class PersonList(list, Sortable, Searchable):
    """
    This class has no instance variables.
    The list data is held in the parent list class object
    The constructor must call the list constructor: See Tower 
    Code a populate method, which reads the CSV file.
       It must use: try / except, csv.reader, with open
    Code the sort method: Must accept a function object
    Code the search method: Must accept function and search objects
    Code a __str__ method: Look at Tower for help
    You may want to code a person_at method for debug purposes.
    This takes an index and returns the Person at that location.
    """ 
    def __init__(self):
        super().__init__()

    def populate(self, file):
        try:
            with open(file, 'r') as input_file:
                lines = csv.reader(input_file)
                person_list = list(lines)
                for pers in person_list:
                    name = pers[0].strip()
                    month = int(pers[1])
                    day = int(pers[2])
                    year = int(pers[3])
                    self.append(Person(name, year, month, day))
        except IOError:
            print("File Open Error.")

    def sort(self, func):
        return func(self)

    def search(self, func, obj):
        return func(self, obj)

    def __str__(self):
        p_string = ""
        for person in self:
            p_string = p_string + str(person) + "\n"
        return p_string
