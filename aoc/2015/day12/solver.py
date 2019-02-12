#!/usr/bin/env python3

import json

INPUT = 'input.txt'
text = open(INPUT).read()

def store_all_elements_of_in(d, counter):
    if type(d) is dict:
        if not 'red' in d.values():
            for k, v in d.items():
                counter = store_all_elements_of_in(v, counter)
    elif type(d) is list:
        for e in d:
            counter = store_all_elements_of_in(e, counter)
    elif type(d) is int:
        return counter + d
    return counter

js = json.loads(text)

sum_integers = store_all_elements_of_in(js, 0)
print(sum_integers)
