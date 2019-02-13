#!/usr/bin/env python3

from itertools import permutations

INPUT = 'input.txt'
text = open(INPUT).read()

all_infos = {}
for l in text.split('\n'):
    name, _, _, distance, _, _, time, _, _, _, _, _, _, rest, _ = l.split()
    all_infos[name] = {
        'distance': int(distance),
        'time': int(time),
        'rest': int(rest),
        'current': 0,
        'rest_time_remaining': 0,
        'energy_remaining': int(time),
        'points': 0,
    }

def get_max_distance(d):
    return max([v['current'] for v in d.values()])

for _ in range(2503):
    for k, v in all_infos.items():
        if v['rest_time_remaining'] > 0:
            all_infos[k]['rest_time_remaining'] -= 1
        else:
            all_infos[k]['current'] += all_infos[k]['distance']
            all_infos[k]['energy_remaining'] -= 1
            if all_infos[k]['energy_remaining'] == 0:
                all_infos[k]['rest_time_remaining'] = all_infos[k]['rest']
                all_infos[k]['energy_remaining'] = all_infos[k]['time']

    max_distance = get_max_distance(all_infos)
    for k, v in all_infos.items():
        all_infos[k]['points'] += 1 if v['current'] == max_distance else 0

print(get_max_distance(all_infos))
print(max([v['points'] for v in all_infos.values()]))