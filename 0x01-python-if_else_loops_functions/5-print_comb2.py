#!/usr/bin/python3
for number in range (0, 10):
    for number2 in range(0, 10):
        if number == 9 and number2 == 9:
            print("{}{}".format(number, number2))
        else:
            print("{}{}".format(number, number2), end = ', ')
