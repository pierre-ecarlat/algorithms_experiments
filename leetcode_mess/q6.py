"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
------------------------------
Longest Substring Without Repeating Characters 
------------------------------
Given a string, find the length of the longest substring without repeating 
characters.


Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.

Note that the answer must be a substring, "pwke" is a subsequence and not a 
substring.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import numpy as np

examples = [
  { 'word': 'abcabcbb', 'result': 3 },
  { 'word': 'bbbbb',    'result': 1 },
  { 'word': 'pwwkew',   'result': 3 },
]


def solve(params):
  seq = params['word']
  
  max_l = 0
  sseq = []
  for elmt in seq:
    if elmt in sseq:
      sseq = []
    sseq.append(elmt)
    if len(sseq) > max_l:
      max_l = len(sseq)

  return max_l


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





