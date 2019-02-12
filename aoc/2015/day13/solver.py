#!/usr/bin/env python3

from itertools import permutations

INPUT = 'input.txt'
text = open(INPUT).read()


def get_happiness(permutations):
    maximum_happiness_level = -10000
    for perm in permutations:
        happiness_level = 0
        for i in range(len(perm)-1):
            pp1 = perm[i]
            pp2 = perm[i+1]
            happiness_level += happiness[pp1][pp2] + happiness[pp2][pp1]
        happiness_level += happiness[perm[-1]][perm[0]]
        happiness_level += happiness[perm[0]][perm[-1]]
        if happiness_level > maximum_happiness_level:
            maximum_happiness_level = happiness_level
    return maximum_happiness_level

def get_permutations(people):
    # Circular table, so I can leave one person at the same place
    # Much faster
    perms = permutations(people[1:])
    return [(people[0],) + p for p in list(perms)]

happiness = dict()
for l in text.split('\n'):
    pp1, _, action, nb, _, _, _, _, _, _, pp2 = l[:-1].split()
    positiveness = (1 if action == 'gain' else -1)
    happiness.setdefault(pp1, {})[pp2] = int(nb) * positiveness
all_pp = list(happiness.keys())

all_permutations = get_permutations(all_pp)
maximum_happiness_level = get_happiness(all_permutations)
print(maximum_happiness_level)

# Add myself
MY_NAME = 'ME'
for pp in all_pp:
    happiness.setdefault(MY_NAME, {})[pp] = 0
    happiness[pp][MY_NAME] = 0
all_pp.append(MY_NAME)

all_permutations = get_permutations(all_pp)
maximum_happiness_level = get_happiness(all_permutations)
print(maximum_happiness_level)