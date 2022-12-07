#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dictionary_cpy = a_dictionary.copy()
    keyslst = list(dictionary_cpy.key())
    for key in keyslst:
        dictionary_cpy[key] *= 2
    return (dictionary_cpy)
