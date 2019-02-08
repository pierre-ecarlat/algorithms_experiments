#!/usr/bin/env python

import time


def solve_part1(c):
  c += c[0]
  vals = [int(c[i]) for i in range(len(c)-1) if (c[i] == c[i+1])]
  return sum(vals)

def solve_part2(c):
  halfway = len(c) / 2
  rc = c[halfway:] + c[:halfway]
  vals = [int(c[i]) for i in range(len(c)) if (c[i] == rc[i])]
  return sum(vals)


if __name__ == '__main__':

  # Reader
  ipt = open('input.md').read().rstrip()

  t_start = time.time()
  answer = solve_part1(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))

  t_start = time.time()
  answer = solve_part2(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))








