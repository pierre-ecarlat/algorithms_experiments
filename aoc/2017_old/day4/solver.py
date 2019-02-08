#!/usr/bin/env python

import time


def solve_part1(c):
  return sum([1 for x in c if len(set(x)) == len(x)])

def solve_part2(c):
  c = [[''.join(sorted(e)) for e in x] for x in c]
  return sum([1 for x in c if len(set(x)) == len(x)])

if __name__ == '__main__':

  # Reader
  ipt = [[e for e in l.split()] for l in open('input.md').read().split('\n')]
  
  t_start = time.time()
  answer = solve_part1(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))

  t_start = time.time()
  answer = solve_part2(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))








