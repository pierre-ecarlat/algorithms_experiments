#!/usr/bin/env python3

examples_part1 = {
    '2x3x4': 58,
    '1x1x10': 43,
    '2x3x4\n1x1x10': 101,
}

examples_part2 = {
    '2x3x4': 34,
    '1x1x10': 14,
    '2x3x4\n1x1x10': 48,
}

INPUT = 'input.txt'

def computePaper(line):
    l, w, h = [int(c) for c in line]
    lw = l*w
    lh = l*h
    wh = w*h
    return 2*lw + 2*lh + 2*wh + min(lw, lh, wh)

def computeRibbon(line):
    l, w, h = [int(c) for c in line]
    return 2*(l+w+h) - 2*max(l,w,h) + l*w*h

def solve_part1(ipt):
    lines = [l.split('x') for l in ipt.split('\n')]
    return sum(computePaper(l) for l in lines)

def solve_part2(ipt):
    lines = [l.split('x') for l in ipt.split('\n')]
    return sum(computeRibbon(l) for l in lines)

def test(name, d, func):
    for key, val in d.items():
        assert func(key) == val, 'Problem with ' + key
    print("Test " + name + ": All success.")


if __name__ == '__main__':

    test("part1", examples_part1, solve_part1)
    test("part2", examples_part2, solve_part2)

    # Reader
    ipt = open(INPUT).read()
    total_paper = solve_part1(ipt)
    print(total_paper)
    total_ribbon = solve_part2(ipt)
    print(total_ribbon)