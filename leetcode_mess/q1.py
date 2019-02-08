"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
------------------------------
Single Element in a Sorted Array 
------------------------------

Given a sorted array consisting of only integers where every element appears 
twice except for one element which appears once. Find this single element that 
appears only once. 


Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10


Note:
Your solution should run in O(log n) time and O(1) space.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

examples = [
  { 'array': [1,1,2,3,3,4,4,8,8], 'result': 2 }, 
  { 'array': [3,3,7,7,10,11,11],  'result': 10 }, 
]


def solve(params):
  array = params['array']

  while True:
    if len(array) == 1:
      return array[0]

    m = len(array) / 2
    if array[m] == array[m+1]:
      if m % 2 == 0:
        array = array[m+2:]
      else:
        array = array[:m]

    elif array[m] == array[m-1]:
      if m % 2 == 0:
        array = array[:m-1]
      else:
        array = array[m+1:]

    else:
      return array[m]


def main():
  # Check all the study cases
  for ix, ex in enumerate(examples):
    out = solve(ex)
    assert out == ex['result'], \
        'Wrong result for example {} ({}, should be {})'.\
        format(ix+1, out, ex['result'])
  
  print('Success!')

if __name__=='__main__':
  main()
  print('')





