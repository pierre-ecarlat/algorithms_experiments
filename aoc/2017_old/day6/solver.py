#!/usr/bin/env python

import time
import numpy as np

def solve_part1(c):
  size = len(c)
  count = 0
  list_states = []
  while c not in list_states:
    list_states.append(c[:])
    count += 1

    argmax = np.argmax(c)
    value = c[argmax]
    c[argmax] = 0
    ix = (argmax + 1) % size
    for ix in range(value):
      c[(argmax + ix + 1) % size] += 1
  
  return count


def solve_part2(c):
  size = len(c)
  count = 0
  first = c[:]
  while True:
    count += 1
    argmax = np.argmax(c)
    value = c[argmax]
    c[argmax] = 0
    ix = (argmax + 1) % size
    for ix in range(value):
      c[(argmax + ix + 1) % size] += 1
  
    if c == first:
      break
  
  return count

if __name__ == '__main__':

  # Reader
  ipt = [int(l) for l in open('input.md').read().split('\t')]
  #ipt = [0,2,7,0]

  t_start = time.time()
  answer = solve_part1(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))

  t_start = time.time()
  answer = solve_part2(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))








