"""
 Project Name: Project1
 Filename: person_sort_main.py
 Programmer: Alex Lopez Torres Riega
 Date: September 25, 2018

 Description:
    Object-oriented program that implements several sorting algorithms
    of different algorithm complexities. Differently ordered files are
    then sorted using several algorithms and the number of comparisons
    are displayed.

"""

from comparable import Comparable
from person import Person
from personList import PersonList
from sort_search_funcs import *


def main():
    print("Sorting the 32 element Person file")
    print("==================================")
    print()

    func_list = [selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort]

    file_name = "Person32.csv"
    file_size = file_name[6:8]

    for func in func_list:
        p_list = PersonList()
        p_list.populate(file_name)
        p_list.sort(func)
        print("Sorting", file_size, "file", file_name, "using", func.__name__)
        print("The number of compares are", Comparable.get_num_compares())
        print()
        print("The sorted list is:")
        print(p_list)
        Comparable.clear_compares()

    print("Sorting the 4 different sized random Person files")
    print("=================================================")
    print()

    random_files = ["Person1Ka.csv", "Person2Ka.csv", "Person4Ka.csv", "Person8Ka.csv"]

    for func in func_list:
        for file in random_files:
            file_size = file[6:8]
            p_list = PersonList()
            p_list.populate(file)
            p_list.sort(func)
            print("Sorting", file_size, "file", file, "using", func.__name__)
            print("The number of compares are", Comparable.get_num_compares())
            Comparable.clear_compares()
            print()

    print("Sorting the 4 different sized sorted Person files")
    print("=================================================")
    print()

    sorted_files = ["Person1Kb.csv", "Person2Kb.csv", "Person4Kb.csv","Person8Kb.csv"]

    for func in func_list:
        for file in sorted_files:
            file_size = file[6:8]
            p_list = PersonList()
            p_list.populate(file)
            p_list.sort(func)
            print("Sorting", file_size, "file", file, "using", func.__name__)
            print("The number of compares are", Comparable.get_num_compares())
            Comparable.clear_compares()
            print()

    print("Sorting the 4 different sized reverse sorted Person files")
    print("=========================================================")
    print()

    reverse_files = ["Person1Kc.csv", "Person2Kc.csv", "Person4Kc.csv","Person8Kc.csv" ]

    for func in func_list:
        for file in reverse_files:
            file_size = file[6:8]
            p_list = PersonList()
            p_list.populate(file)
            p_list.sort(func)
            print("Sorting", file_size, "file", file, "using", func.__name__)
            print("The number of compares are", Comparable.get_num_compares())
            Comparable.clear_compares()
            print()

main()
