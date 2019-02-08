#!/usr/bin/env python

import time
import math
import numpy as np

def solve_part1(c):
  vertice_size = math.ceil(math.sqrt(c))
  if vertice_size % 2 == 0: vertice_size += 1
  square_nb = int((vertice_size - 1) / 2)
  max_val = pow(vertice_size, 2)
  distance = max_val - c
  res = square_nb
  desc = -1
  
  for _ in range(int(distance)):
    res += desc
    if res == 0 or res == square_nb:
      desc *= -1
  return square_nb + res

def solve_part2(c):
  matrix = np.zeros((11,11))
  start = (5,5)
  position = start
  matrix[position] = 1
  RIGHT  = (0,1)
  TOP    = (-1,0)
  LEFT   = (0,-1)
  BOTTOM = (1,0)
  direction = RIGHT

  while matrix[position] < c:
    position = tuple(map(sum, zip(position, direction)))
    matrix[position] = matrix[position[0]-1:position[0]+2, 
                              position[1]-1:position[1]+2].sum()
    
    if direction == RIGHT and matrix[tuple(map(sum, zip(position, TOP)))] == 0:
      direction = TOP
    elif direction == TOP and matrix[tuple(map(sum, zip(position, LEFT)))] == 0:
      direction = LEFT
    elif direction == LEFT and matrix[tuple(map(sum, zip(position, BOTTOM)))] == 0:
      direction = BOTTOM
    elif direction == BOTTOM and matrix[tuple(map(sum, zip(position, RIGHT)))] == 0:
      direction = RIGHT

  return matrix[position]

if __name__ == '__main__':

  # Reader
  ipt = int(open('input.md').read().rstrip())

  t_start = time.time()
  answer = solve_part1(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))

  t_start = time.time()
  answer = solve_part2(ipt)
  t_stop = time.time()

  print('Found {0} in {1:.3f}ms.'.format(answer, (t_stop - t_start)*1000))








