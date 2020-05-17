# Coin Flip Streaks: this programs finds out how many times you can generate a streak of 6 heads or 6 tails in a coin flip game

import random

# these variables count the streak of 6 heads and 6 tails respectively
headCount = 0   # count the head
streakHead = 0  # count the streak of 6 heads
tailCount = 0   # count the tail
streakTail = 0  # count the streak of 6 tails

flipCoin = ['H','T']

for i in range(10000):

    if random.choice(flipCoin) == 'H':
        headCount += 1
    else:
        tailCount += 1

    if headCount == 6:
        headCount = 0
        streakHead += 1

    if tailCount == 6:
        tailCount = 0
        streakTail += 1
    
print('In 10000 coins flip, here is the result:', end='\n ')
print('Number of streak of six heads: ',streakHead, end='\n ')
print('Number of streak of six tails: ', streakTail)
    

