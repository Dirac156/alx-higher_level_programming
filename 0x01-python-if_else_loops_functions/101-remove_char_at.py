#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0:
        return str
    i = 0
    new = ""
    for element in str:
        if i == n:
            continue
        new += str[i]
    return new
