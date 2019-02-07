#!/usr/bin/env python3

import time
import hashlib

examples_part1 = {
    'abcdef': 609043,
    'pqrstuv': 1048970,
}

examples_part2 = {
}

INPUT = 'input.txt'

def getHash(text):
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def solve_part1(ipt):
    decimal_to_find = 1
    while(1):
        computed_hash = getHash(ipt + str(decimal_to_find))
        if computed_hash[:5] == '00000':
            return decimal_to_find
        decimal_to_find += 1

def solve_part2(ipt):
    decimal_to_find = 1
    while(1):
        computed_hash = getHash(ipt + str(decimal_to_find))
        if computed_hash[:6] == '000000':
            return decimal_to_find
        decimal_to_find += 1

def test(name, d, func):
    print("==================")
    print("Test all the examples for " + name)
    for i, (key, val) in enumerate(d.items()):
        start = time.time()
        success = func(key) == val
        time_spent = time.time() - start
        if success:
            print("\tOK: Test " + str(i) + " in: " + str(time_spent))
        else:
            print("\tFAILED: Test " + i + " (key " + key + ")")


if __name__ == '__main__':

    test("part1", examples_part1, solve_part1)
    test("part2", examples_part2, solve_part2)

    # Reader
    ipt = open(INPUT).read()
    final_decimal = solve_part1(ipt)
    print(final_decimal)
    final_decimal = solve_part2(ipt)
    print(final_decimal)