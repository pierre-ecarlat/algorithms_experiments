"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
------------------------------
Two Sum 
------------------------------
Given an array of integers, return indices of the two numbers such that they 
add up to a specific target. You may assume that each input would have exactly 
one solution, and you may not use the same element twice.


Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import numpy as np

examples = [
  { 'array': [2,7,11,15], 'target': 9, 'result': [0,1] },
]


def solve(params):
  array = params['array']
  target = params['target']
  
  for ix1, item1 in enumerate(array):
    for ix2, item2 in enumerate(array[ix1+1:]):
      if item1 + item2 == target:
        return [ix1, ix1 + ix2 + 1]

  return None


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





