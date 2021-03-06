#!/usr/bin/env python3

import time

examples_part1 = {
    '>': 2,
    '^>v<': 4,
    '^v^v^v^v^v': 2,
}

examples_part2 = {
    '^v': 3,
    '^>v<': 3,
    '^v^v^v^v^v': 11,
}

INPUT = 'input.txt'

def getMove(direction):
    return {
        'v': (1, 0),
        '^': (-1, 0),
        '>': (0, 1),
        '<': (0, -1),
    }[direction]

def moveSanta(position, direction):
    move = getMove(direction)
    return (position[0] + move[0], position[1] + move[1])

def solve_part1(ipt):
    current = (0,0)
    locations = [current]
    for direction in ipt:
        current = moveSanta(current, direction)
        if current not in locations:
            locations.append(current)
    return len(locations)

def solve_part2(ipt):
    currentSanta = (0,0)
    currentRobotSanta = (0,0)
    locations = [currentSanta, currentRobotSanta]
    for i, direction in enumerate(ipt):
        if i % 2 == 1:
            currentSanta = moveSanta(currentSanta, direction)
            locations.append(currentSanta)
        else:
            currentRobotSanta = moveSanta(currentRobotSanta, direction)
            locations.append(currentRobotSanta)

    return len(set(locations))

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
            print("\tFAILED: Test " + i + " (key " + key + ")")


if __name__ == '__main__':

    test("part1", examples_part1, solve_part1)
    test("part2", examples_part2, solve_part2)

    # Reader
    ipt = open(INPUT).read()
    total_houses = solve_part1(ipt)
    print(total_houses)
    total_houses = solve_part2(ipt)
    print(total_houses)