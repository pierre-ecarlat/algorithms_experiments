#!/usr/bin/env python3

import itertools

INPUT = 'input.txt'
buckets = [int(l) for l in open(INPUT).read().split('\n')]

counter = 0
for L in range(len(buckets)):
    for subset in itertools.combinations(buckets, L + 1):
        if sum(subset) == 150:
            counter += 1
    if counter != 0:
        break

print(counter)