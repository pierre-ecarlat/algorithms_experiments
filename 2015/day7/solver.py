#!/usr/bin/env python3

import time
import numpy as np

examples_part1 = {
    '123 -> x\n'        +\
    '456 -> y\n'        +\
    'x AND y -> d\n'    +\
    'x OR y -> e\n'     +\
    'x LSHIFT 2 -> f\n' +\
    'y RSHIFT 2 -> g\n' +\
    'NOT x -> h\n'      +\
    'NOT y -> i':        \
    { 'd': 72, 'e': 507, 'f': 492, 'g': 114, 'h': 65412, 'i': 65079,
      'x': 123, 'y': 456 },
}

examples_part2 = {
}

INPUT = 'input.txt'

def get_16bits(decimal):
    return '{0:016b}'.format(decimal)

def get_decimal(bits):
    return int(bits, 2)

def gate_AFFECT(val):
    return val

def gate_NOT(s):
    return s.replace('1', '2').replace('0', '1').replace('2', '0')

def gate_AND(s1, s2):
    return ''.join(['1' if e1 + e2 == '11' else '0' for e1, e2 in zip(s1, s2)])

def gate_OR(s1, s2):
    return ''.join(['1' if e1 + e2 != '00' else '0' for e1, e2 in zip(s1, s2)])

def gate_LSHIFT(s, value):
    value = get_decimal(value)
    return (s + ''.join(['0' for i in range(value)]))[value:]

def gate_RSHIFT(s, value):
    value = get_decimal(value)
    return (''.join(['0' for i in range(value)]) + s)[:-value]

def decodeInstruction(text):
    gate = ''
    inputs = []
    tmp = text.split(' -> ')

    part1 = tmp[0].split(' ')
    if len(part1) == 1:
        gate = 'AFFECT'
        inputs.append(tmp[0])
    elif len(part1) == 2:
        gate = 'NOT'
        inputs.append(part1[1])
    else:
        gate = part1[1]
        inputs.append(part1[0])
        inputs.append(part1[2])

    return gate, inputs, tmp[1]

def allocator(name):
    return {
        'AFFECT': gate_AFFECT,
        'NOT': gate_NOT,
        'AND': gate_AND,
        'OR': gate_OR,
        'LSHIFT': gate_LSHIFT,
        'RSHIFT': gate_RSHIFT,
    }[name]

def executeInstructionOn(gate, inputs, output, wires):
    inputs = [wires[i] if i in wires else get_16bits(int(i)) for i in inputs]
    operator_to_use = allocator(gate)
    wires[output] = operator_to_use(*inputs)
    return wires

def couldBeInt(s):
    try:
        int(s)
    except ValueError:
        return False
    return True

def canIDoIt(inputs, wires):
    return all([i in wires or couldBeInt(i) for i in inputs])

def solve_part1(ipt):
    instructions = ipt.split('\n')
    wires = {}
    while len(instructions) > 0:
        gate, inputs, output = decodeInstruction(instructions[0])
        if canIDoIt(inputs, wires):
            wires = executeInstructionOn(gate, inputs, output, wires)
            instructions.pop(0)
        else:
            instructions.append(instructions.pop(0))
    for key, val in wires.items():
        wires[key] = get_decimal(val)
    return wires

def solve_part2(ipt):
    instructions = ipt.split('\n')
    wires = {}
    while len(instructions) > 0:
        gate, inputs, output = decodeInstruction(instructions[0])
        if canIDoIt(inputs, wires):
            if gate == 'AFFECT' and output == 'b':
                inputs[0] = 956
            wires = executeInstructionOn(gate, inputs, output, wires)
            instructions.pop(0)
        else:
            instructions.append(instructions.pop(0))
    for key, val in wires.items():
        wires[key] = get_decimal(val)
    return wires

def compareDictionaries(d1, d2):
    return all([v == d2[k] for k, v in d1.items()])

def test(name, d, func):
    print("==================")
    print("Test all the examples for " + name)
    for i, (key, val) in enumerate(d.items()):
        start = time.time()
        success = compareDictionaries(func(key), val)
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
    final_wires = solve_part1(ipt)
    print(final_wires['a'])
    final_wires = solve_part2(ipt)
    print(final_wires['a'])