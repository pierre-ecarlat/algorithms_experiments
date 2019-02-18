#!/usr/bin/env python3

import time

start = time.time()

def all_divisors(n):
    step = 2 if n%2 else 1
    all_potential = range(1, int(n**0.5)+1, step)
    divs = set()
    for i in [e for e in all_potential if n % e == 0]:
        divs.add(i)
        divs.add(n//i)
    return divs

INPUT = 'input.txt'
number = int(open(INPUT).read())
part_one, part_two = None, None
i = 0
while not (part_one and part_two):
    i += 1
    divisors = all_divisors(i)
    if not part_one:
        if sum(divisors) * 10 >= number:
            part_one = i
    if not part_two:
        if sum(d for d in divisors if i / d <= 50) * 11 >= number:
            part_two = i

print(part_one)
print(part_two)

print(time.time() - start)
