#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dic = {}
    for keys in a_dictionary.keys():
        if keys == key:
            new_dic[key] = value
        else:
            new_dic[keys] = a_dictionary[keys]
    return new_dic
