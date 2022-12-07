#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    keyslist = list(a_dictionary.keys())
    for i in keyslist:
        count = count + 1
    return (count)
