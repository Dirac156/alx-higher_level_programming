#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dic = a_dictionary.copy()
    new_dic[key] = value
    return new_dic
