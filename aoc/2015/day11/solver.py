#!/usr/bin/env python3

INPUT = 'input.txt'
ASC_A = 97
ASC_I = 105
ASC_L = 108
ASC_O = 111
ASC_Z = 122

text = open(INPUT).read()

def plus_one(text, _id):
    text[_id] += 1
    if text[_id] > ASC_Z:
        text[_id] = ASC_A
        return plus_one(text, _id-1)
    else:
        return text

def check_conditions(s):
    if ASC_I in s or ASC_L in s or ASC_O in s:
        return False

    two_pairs = 0
    skip = False
    for i in range(len(s)-1):
        if skip:
            skip = False
        elif s[i] == s[i+1]:
            two_pairs += 1
            skip = True

    three_letters = False
    if s[0] == s[1]:
        two_pairs.add(s[0])
    for i in range(len(s)-2):
        if s[i] == s[i+1]-1 and s[i+1] == s[i+2]-1:
            three_letters = True

    return three_letters and two_pairs >= 2

def get_new_password(passwd):
    passwd = [ord(c) for c in passwd]
    while 1:
        passwd = plus_one(passwd, -1)
        if check_conditions(passwd):
            break
    return ''.join([chr(c) for c in passwd])

print(get_new_password(text))
print(get_new_password(get_new_password(text)))
