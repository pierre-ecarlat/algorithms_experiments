#!/usr/bin/env python3

import numpy as np

NB_STEPS = 100
WIDTH = 100
HEIGHT = 100

INPUT = 'input.txt'
text = open(INPUT).read().split('\n')

lights = np.zeros((WIDTH+2, HEIGHT+2))
for i in range(1, WIDTH+1):
    for j in range(1, HEIGHT+1):
        if text[i-1][j-1] == '#':
            lights[i,j] = 1
lights[1,1] = lights[1,100] = lights[100,1] = lights[100,100] = 1

for _ in range(NB_STEPS):
    tmp_lights = np.copy(lights)
    for i in range(1, WIDTH+1):
        for j in range(1, HEIGHT+1):
            neighb = np.count_nonzero(tmp_lights[i-1:i+2,j-1:j+2])
            if (tmp_lights[i,j] == 0 and neighb == 3):
                lights[i,j] = 1
            elif tmp_lights[i,j] == 1 and neighb != 3 and neighb != 4:
                lights[i,j] = 0
    lights[1,1] = lights[1,100] = lights[100,1] = lights[100,100] = 1

print(np.count_nonzero(lights))