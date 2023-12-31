#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not roman_string or not isinstance(roman_string, str)):
        return (0)

    roman_list = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    value = 0
    for i in range(len(roman_string)):
        if (i+1 != len(roman_string) and
                roman_list[roman_string[i]] < roman_list[roman_string[i+1]]):
            value -= roman_list[roman_string[i]]
        else:
            value += roman_list[roman_string[i]]

    return (value)
