"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
------------------------------
Coin Change 2 
------------------------------

You are given coins of different denominations and a total amount of money. 
Write a function to compute the number of combinations that make up that 
amount. You may assume that you have infinite number of each kind of coin.


Note: 
You can assume that
 0 <= amount <= 5000
 1 <= coin <= 5000
 the number of coins is less than 500 
 the answer is guaranteed to fit into signed 32-bit integer


Example 1:
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10] 
Output: 1
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import numpy as np

examples = [
  { 'amount': 5,  'coins': [1,2,5], 'result': 4 }, 
  { 'amount': 3,  'coins': [2],     'result': 0 }, 
  { 'amount': 10, 'coins': [10],    'result': 1 }, 
]


def solve(params):
  amount = params['amount']
  coins = params['coins']

  dp = [0] * (amount + 1)
  dp[0] = 1
  for c in coins:
    for x in range(c, amount+1):
      dp[x] += dp[x - c]
  return dp[amount]


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





