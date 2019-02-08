#!/usr/bin/env python

import time


def solve_part1(c):
  return sum([max(x) - min(x) for x in c])

def solve_part2(c):
  s = 0
  for l in c:
    l = sorted(l, reverse=True)
    for _x, v1 in enumerate(l):
      for v2 in l[_x+1:]:
        if v1 % v2 == 0:
          s += v1 / v2
          break
  return s

if __name__ == '__main__':

  # Reader
  ipt = [[int(e) for e in l.split('\t')] 
                 for l in open('input.md').read().split('\n')]
  
  t_start = time.time()
  answer = solve_part1(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))

  t_start = time.time()
  answer = solve_part2(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))








