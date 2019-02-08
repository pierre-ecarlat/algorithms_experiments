#!/usr/bin/env python3

INPUT = 'input.txt'

value = open(INPUT).read()

def decompose(s):
    vals = [s[0]]
    nbs = [1]
    for e in s[1:]:
        if e == vals[-1]:
            nbs[-1] += 1
        else:
            vals.append(e)
            nbs.append(1)
    return vals, nbs

for _ in range(50):
    vals, nbs = decompose(value)
    value = ''.join([str(n) + v for v, n in zip(vals, nbs)])

print(len(value))