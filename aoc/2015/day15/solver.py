#!/usr/bin/env python3

# Brute force... should perform linear regression or any optimization method
# TODO TODO TODO

import numpy as np
from constraint import *

INPUT = 'input.txt'

def get_ingredients_from(text):
    ingredients = {}
    for ligne in text.split('\n'):
        detail = ligne.split()
        ingredients.setdefault('names', []).append(detail[0][:-1])
        ingredients.setdefault('capacities', []).append(int(detail[2][:-1]))
        ingredients.setdefault('durabilities', []).append(int(detail[4][:-1]))
        ingredients.setdefault('flavors', []).append(int(detail[6][:-1]))
        ingredients.setdefault('textures', []).append(int(detail[8][:-1]))
        ingredients.setdefault('calories', []).append(int(detail[10]))
    return ingredients

def get_all_possible_combinations(ingredients_names, nb_units):
    problem = Problem()
    for name in ingredients_names:
        problem.addVariable(name, range(nb_units+1))
    problem.addConstraint(ExactSumConstraint(nb_units))
    return problem.getSolutions()

def compute_score(balance, ingredients):
    balance = np.array(balance)
    capacities = np.array(ingredients['capacities'])
    durabilities = np.array(ingredients['durabilities'])
    flavors = np.array(ingredients['flavors'])
    textures = np.array(ingredients['textures'])
    return max(sum(capacities * balance), 0) * \
           max(sum(durabilities * balance), 0) * \
           max(sum(flavors * balance), 0) * \
           max(sum(textures * balance), 0)

def is_500_calories(balance, ingredients):
    balance = np.array(balance)
    calories = np.array(ingredients['calories'])
    return sum(calories * balance) == 500

def brute_force_method(ingredients, combinations):
    best_recipe = { 'score': -1 }
    for combination in combinations:
        balance = [combination[name] for name in ingredients['names']]
        if is_500_calories(balance, ingredients):
            score = compute_score(balance, ingredients)
            if score > best_recipe['score']:
                best_recipe = { 'balance': balance, 'score': score }

    return best_recipe

ingredients = get_ingredients_from(open(INPUT).read())
combinations = get_all_possible_combinations(ingredients['names'], 100)
recipe = brute_force_method(ingredients, combinations)

print(recipe)