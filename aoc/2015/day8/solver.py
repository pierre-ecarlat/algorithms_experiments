#!/usr/bin/env python3

INPUT = 'input.txt'

print(sum(len(l) - 1 - len(eval(l)) for l in open(INPUT)) + 1)
print(sum(l.count('\\') + l.count('"') + 2 for l in open(INPUT)))