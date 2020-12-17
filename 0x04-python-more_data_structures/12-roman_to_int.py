#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str) == False or roman_string is None:
        return 0
    numb_r = 0
    lst = []
    for l in roman_string:
        lst.append(l)
    i = 0
    roman_symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
               'C': 100, 'D': 500, 'M': 1000}
    for symbol in lst:
        if symbol not in roman_symbol:
            return 0
        else:
            idx = lst.index(symbol)
            if symbol == lst[-1] or \
                roman_symbol[symbol] >= roman_symbol[lst[idx + 1]]:
                numb_r += roman_symbol[symbol]
            else:
                numb_r -= roman_symbol[symbol]
    return numb_r
