"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
------------------------------
Find All Duplicates in an Array 
------------------------------
Given an array of integers, 1 &le; a[i] &le; n (n = size of array), some 
elements appear twice and others appear once.
Find all the elements that appear twice in this array.
Could you do it without extra space and in O(n) runtime?


Example:
Input:
[4,3,2,7,8,2,3,1]
Output:
[2,3]
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import numpy as np

examples = [
  { 'array': [4,3,2,7,8,2,3,1], 'result': [2,3] },
]


def solve(params):
  array = params['array']
  
  already_seen = []
  for item in array:
    if array[abs(item)-1] > 0:
      array[abs(item)-1] *= -1
    else:
      already_seen.append(abs(item))
  
  return already_seen


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





