#!/usr/bin/env python3

import sys

INPUT = 'input.txt'
text = open(INPUT).read().split('\n')

keys = {}
vals = {}
while text[0] != '':
    a, _, b = text[0].split()
    keys.setdefault(a, [])
    keys[a].append(b)
    vals.setdefault(b, [])
    vals[b].append(a)
    text = text[1:]

molecule_to_find = text[1]

def get_variations(current, keys):
    new_molecules = set()
    max_lenk = max([len(x) for x in keys])
    for lenk in range(1, max_lenk+1):
        for i in range(0, len(current) - lenk + 1):
            subset = current[i:i+lenk]
            for val in keys.get(subset, []):
                new_molecules.add(current[0:i] + val + current[i+lenk:])

    return new_molecules

# Part 1
print(len(get_variations(molecule_to_find, keys)))

# Part 2
def get_shortest_index(l):
    lengths = [x['l'] for x in l]
    return lengths.index(min(lengths))

checked = []
variations = []
variations.append({'m': molecule_to_find, 'c': 0, 'l': len(molecule_to_find)})
while 1:
    shortest_idx = get_shortest_index(variations)
    shortest = variations[shortest_idx]
    checked.append(shortest['m'])
    del variations[shortest_idx]
    new_molecules = get_variations(shortest['m'], vals)
    for m in new_molecules:
        if m == 'e':
            print(shortest['c']+1)
            sys.exit()
        elif not m in checked:
            variations.append({'m': m, 'c': shortest['c']+1, 'l': len(m)})
