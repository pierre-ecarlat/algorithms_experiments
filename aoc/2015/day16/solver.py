#!/usr/bin/env python3

import re

INPUT = 'input.txt'
MFCSAM_results = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

text = open(INPUT).read()

all_sues = []
for ligne in text.split('\n'):
    infos = re.split(', |: ', ligne)[1:]
    nb_characts = int(len(infos) / 2)
    all_characts = [infos[i*2] for i in range(nb_characts)]
    all_values = [int(infos[i*2+1]) for i in range(nb_characts)]
    all_sues.append({
        charact: value for charact, value in zip(all_characts, all_values)
    })

# Part 1
matching_sues = []
for i_sue, sue in enumerate(all_sues):
    if all([v == MFCSAM_results[k] for k, v in sue.items()]):
        matching_sues.append(i_sue + 1)

print(matching_sues)

# Part 2
greater_than = ['cats', 'trees']
fewer_than = ['pomeranians', 'goldfish']
equal_to = ['children', 'samoyeds', 'akitas', 'vizslas', 'cars', 'perfumes']

matching_sues = []
for i_sue, sue in enumerate(all_sues):
    if all([(k in equal_to and v == MFCSAM_results[k]) or \
            (k in greater_than and v > MFCSAM_results[k]) or \
            (k in fewer_than and v < MFCSAM_results[k]) \
       for k, v in sue.items()]):
        matching_sues.append(i_sue + 1)

print(matching_sues)