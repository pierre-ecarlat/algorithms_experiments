#!/usr/bin/env python3

import time
import numpy as np

examples_part1 = {
    'turn on 0,0 through 999,999': 1000000,
    'turn on 0,0 through 999,999\ntoggle 0,0 through 999,0': 999000,
    'turn off 499,499 through 500,500': 0,
}

examples_part2 = {
    'turn on 0,0 through 0,0': 1,
    'toggle 0,0 through 999,999': 2000000
}

INPUT = 'input.txt'

def extractInstructionFrom(s):
    tmp = s.split(' through ')
    tmp2 = tmp[0].split(' ')
    action = ' '.join(tmp2[:-1])
    topCoords = tuple([int(x) for x in tmp2[-1].split(',')])
    lowCoords = tuple([int(x) for x in tmp[1].split(',')])
    return action, topCoords, lowCoords

def executeOn(text, lights):
    action, topCorner, lowCorner = extractInstructionFrom(text)
    x1, x2, y1, y2 = topCorner[0], lowCorner[0]+1, topCorner[1], lowCorner[1]+1
    if action == 'turn on':
        lights[x1:x2,y1:y2] = 1
    elif action == 'turn off':
        lights[x1:x2,y1:y2] = 0
    elif action == 'toggle':
        lights[x1:x2,y1:y2] = (((lights[x1:x2,y1:y2] * 2 - 1) * -1) + 1) / 2

    return lights

def executeOnTwo(text, lights):
    action, topCorner, lowCorner = extractInstructionFrom(text)
    x1, x2, y1, y2 = topCorner[0], lowCorner[0]+1, topCorner[1], lowCorner[1]+1
    if action == 'turn on':
        lights[x1:x2,y1:y2] += 1
    elif action == 'turn off':
        lights[x1:x2,y1:y2] -= 1
        lights[lights < 0] = 0
    elif action == 'toggle':
        lights[x1:x2,y1:y2] += 2

    return lights

def solve_part1(ipt):
    all_lights = np.zeros((1000, 1000))
    instructions = ipt.split('\n')
    for instruction in instructions:
        all_lights = executeOn(instruction, all_lights)
    return int(np.sum(all_lights))

def solve_part2(ipt):
    all_lights = np.zeros((1000, 1000))
    instructions = ipt.split('\n')
    for instruction in instructions:
        all_lights = executeOnTwo(instruction, all_lights)
    return int(np.sum(all_lights))

def test(name, d, func):
    print("==================")
    print("Test all the examples for " + name)
    for i, (key, val) in enumerate(d.items()):
        start = time.time()
        success = func(key) == val
        time_spent = time.time() - start
        if success:
            print("\tOK: Test " + str(i) + " in: " + str(time_spent))
        else:
            print("\tFAILED: Test " + str(i) + " (key " + key + ")")


if __name__ == '__main__':

    test("part1", examples_part1, solve_part1)
    test("part2", examples_part2, solve_part2)

    # Reader
    ipt = open(INPUT).read()
    number_lights = solve_part1(ipt)
    print(number_lights)
    number_lights = solve_part2(ipt)
    print(number_lights)