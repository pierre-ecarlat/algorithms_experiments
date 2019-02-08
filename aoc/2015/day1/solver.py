#!/usr/bin/env python3

import time

examples_part1 = {
    '(())': 0,
    '()()': 0,
    '(((': 3,
    '(()(()(': 3,
    '))(((((': 3,
    '())': -1,
    '))(': -1,
    ')))': -3,
    ')())())': -3
}

examples_part2 = {
    ')': 1,
    '()())': 5
}

INPUT = 'input.txt'


def solve_part1(ipt):
    floors = [1 if c == '(' else -1 for c in ipt]
    return sum(floors)

def solve_part2(ipt):
    floor = 0
    for i, c in enumerate(ipt):
        floor += 1 if c == '(' else -1
        if floor < 0: break
    return i+1

def test(name, d, func):
    for key, val in d.items():
        assert func(key) == val, 'Problem with ' + key
    print("Test " + name + ": All success.")


if __name__ == '__main__':

    test("part1", examples_part1, solve_part1)
    test("part2", examples_part2, solve_part2)

    # Reader
    ipt = open(INPUT).read()
    final_floor = solve_part1(ipt)
    print(final_floor)
    basement_char = solve_part2(ipt)
    print(basement_char)