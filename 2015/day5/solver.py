#!/usr/bin/env python3

import time

examples_part1 = {
    'ugknbfddgicrmopn': 1,
    'aaa': 1,
    'jchzalrnumimnmhp': 0,
    'haegwjzuvuyypxyu': 0,
    'dvszwmarrgswjxmb': 0,
}

examples_part2 = {
    'qjhvhtzxzqqjkmpb': 1,
    'xxyxx': 1,
    'uurcxstgmygtbstg': 0,
    'ieodomkazucvgmuy': 0
}

INPUT = 'input.txt'
VOYELS = ['a', 'e', 'i', 'o', 'u']
NAUGHTY = ['ab', 'cd', 'pq', 'xy']

def amINice(text):
    twice_in_a_row = False
    number_voyels = int(text[0] in VOYELS)
    for i in range(1, len(text)):
        # If naughty
        if text[i-1:i+1] in NAUGHTY:
            return False
        # Maybe twice in a row?
        if text[i-1] == text[i]:
            twice_in_a_row = True
        # Voyel?
        if text[i] in VOYELS:
            number_voyels += 1

    return twice_in_a_row and number_voyels >= 3

def amINiceTwo(text):
    # First condition
    one_pair_twice = False
    all_pairs = [text[i:i+2] for i in range(0, len(text)-1)]
    for i, pair in enumerate(all_pairs):
        if pair in all_pairs[i+2:]:
            one_pair_twice = True
            break

    # Second condition
    one_letter_between_pair = False
    for i in range(0, len(text)-2):
        if text[i] == text[i+2]:
            one_letter_between_pair = True
            break

    return one_pair_twice and one_letter_between_pair

def solve_part1(ipt):
    lines = ipt.split('\n')
    return sum([1 if amINice(line) else 0 for line in lines])

def solve_part2(ipt):
    lines = ipt.split('\n')
    return sum([1 if amINiceTwo(line) else 0 for line in lines])

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
            print("\tFAILED: Test " + str(i) + " (key " + key + ")")


if __name__ == '__main__':

    test("part1", examples_part1, solve_part1)
    test("part2", examples_part2, solve_part2)

    # Reader
    ipt = open(INPUT).read()
    number_nices = solve_part1(ipt)
    print(number_nices)
    number_nices = solve_part2(ipt)
    print(number_nices)