#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dic = {}
    for keys, values in a_dictionary.items():
        if keys == key:
            new_dic[keys] = value
        else:
            new_dic[keys] = values
    return new_dic
