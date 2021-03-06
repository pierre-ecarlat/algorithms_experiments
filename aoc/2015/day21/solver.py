#!/usr/bin/env python3

import math

shop = {
    'weapons': {
        'Dagger':     { 'cost': 8,  'damage': 4, 'armor': 0 },
        'Shortsword': { 'cost': 10, 'damage': 5, 'armor': 0 },
        'Warhammer':  { 'cost': 25, 'damage': 6, 'armor': 0 },
        'Longsword':  { 'cost': 40, 'damage': 7, 'armor': 0 },
        'Greataxe':   { 'cost': 74, 'damage': 8, 'armor': 0 },
    },
    'armors': {
        'none':       { 'cost': 0,   'damage': 0, 'armor': 0 },
        'Leather':    { 'cost': 13,  'damage': 0, 'armor': 1 },
        'Chainmail':  { 'cost': 31,  'damage': 0, 'armor': 2 },
        'Splintmail': { 'cost': 53,  'damage': 0, 'armor': 3 },
        'Bandedmail': { 'cost': 75,  'damage': 0, 'armor': 4 },
        'Platemail':  { 'cost': 102, 'damage': 0, 'armor': 5 },
    },
    'rings': {
        'none1':      { 'cost': 0,   'damage': 0, 'armor': 0 },
        'none2':      { 'cost': 0,   'damage': 0, 'armor': 0 },
        'Damage_+1':  { 'cost': 25,  'damage': 1, 'armor': 0 },
        'Damage_+2':  { 'cost': 50,  'damage': 2, 'armor': 0 },
        'Damage_+3':  { 'cost': 100, 'damage': 3, 'armor': 0 },
        'Defense_+1': { 'cost': 20,  'damage': 0, 'armor': 1 },
        'Defense_+2': { 'cost': 40,  'damage': 0, 'armor': 2 },
        'Defense_+3': { 'cost': 80,  'damage': 0, 'armor': 3 },
    },
}

INPUT = 'input.txt'
text = open(INPUT).read().split('\n')
boss_stats = {
    'hp': int(text[0].split(': ')[1]),
    'attack': int(text[1].split(': ')[1]),
    'defense': int(text[2].split(': ')[1]),
}
player_stats = {
    'hp': 100,
    'attack': 0,
    'defense': 0,
}

def possible_combinations():
    combinations = []
    for vw in shop['weapons'].values():
        for va in shop['armors'].values():
            for kr1, vr1 in shop['rings'].items():
                for kr2, vr2 in shop['rings'].items():
                    if kr1 == kr2:
                        continue
                    combinations.append({
                        'cost': sum(x['cost'] for x in [vw, va, vr1, vr2]),
                        'attack': sum(x['damage'] for x in [vw, vr1, vr2]),
                        'defense': sum(x['armor'] for x in [va, vr1, vr2])
                    })
    combinations.sort(key = lambda x: x['cost'])
    return list(combinations)

def simulate_game(boss, player):
    player_damages = max(player['attack'] - boss['defense'], 1)
    boss_damages = max(boss['attack'] - player['defense'], 1)

    turns_to_die_boss = math.ceil(boss['hp'] / player_damages)
    turns_to_die_player = math.ceil(player['hp'] / boss_damages)

    return turns_to_die_player >= turns_to_die_boss

min_cost = 999
max_cost = 0
wearables = possible_combinations()
for wearable in wearables:
    player_stats.update(wearable)
    if simulate_game(boss_stats, player_stats):
        min_cost = min(wearable['cost'], min_cost)
    else:
        max_cost = max(wearable['cost'], max_cost)

print('{} {}'.format(min_cost, max_cost))
