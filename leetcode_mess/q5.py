"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
------------------------------
Add Two Numbers 
------------------------------
You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list. 
You may assume the two numbers do not contain any leading zero, except the 
number 0 itself.


Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import numpy as np

examples = [
  { 'llist1': [2,4,3], 'llist2': [5,6,4], 'result': [7,0,8] },
]


def solve(params):
  llist1 = params['llist1']
  llist2 = params['llist2']
  
  count = 0
  for ix, (e1, e2) in enumerate(zip(llist1, llist2)):
    factor = pow(10, ix)
    count += (e1 + e2) * factor
  
  final = []
  while count != 0:
    final.append(count % 10)
    count /= 10

  return final


def main():
  # Check all the study cases
  for ix, ex in enumerate(examples):
    out = solve(ex)
    assert out == ex['result'], \
        'Wrong result for example {} ({}, should be {})'.\
        format(ix+1, out, ex['result'])
  
  print('Success!\n')



if __name__=='__main__':
  main()





