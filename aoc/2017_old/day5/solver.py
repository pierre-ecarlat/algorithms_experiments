#!/usr/bin/env python

import time


def solve_part1(c):
  maze = c[:]
  position = 0
  goal = len(maze)
  count = 0

  while 0 <= position < goal:
    prevPos = position
    position += maze[position]
    maze[prevPos] += 1
    count += 1

  return count

def solve_part2(c):
  maze = c[:]
  position = 0
  goal = len(maze)
  count = 0

  while 0 <= position < goal:
    prevPos = position
    position += maze[position]
    if maze[prevPos] < 3:
      maze[prevPos] += 1
    else:
      maze[prevPos] -= 1
    count += 1

  return count

if __name__ == '__main__':

  # Reader
  ipt = [int(l) for l in open('input.md').read().split('\n')]
  
  t_start = time.time()
  answer = solve_part1(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))

  t_start = time.time()
  answer = solve_part2(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))








