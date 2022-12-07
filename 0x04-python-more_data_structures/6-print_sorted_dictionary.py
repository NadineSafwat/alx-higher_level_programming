#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    listt = list(a_dictionary.keys())
    listt.sort()
    for element in listt:
        print("{}: {}".format(element, a_dictionary.get(element)))
