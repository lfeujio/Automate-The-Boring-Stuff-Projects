# Coin Flip Streaks: this programs finds out how many times you can generate a streak of 6 heads or 6 tails in a coin flip game

import random

# these variables count the streak of 6 heads and 6 tails respectively
headCount = 0   # count the head
streakHead = 0  # count the streak of 6 heads
tailCount = 0   # count the tail
streakTail = 0  # count the streak of 6 tails

totalStreak = 0  # total count of streak of 6 heads or tails 

flipCoin = ['H','T']

for number in range(10000):

    # create list of 100 random coin flip
    coinList = []
    
    for i in range(100):
        coinList += random.choice(flipCoin)


    # Check streak of six headsor tails
    for i in range(len(coinList)-1):
        
        if coinList[i] == coinList[i+1]:
            if coinList[i] == 'H':
                headCount += 1
                
            else:
                tailCount += 1
               

            if headCount == 5:        # Check for a streak of 6. I compare with 5 because a streak of 6 elements has 5 pairs. 
                streakHead += 1
                headCount = 0         #Reinitialize streak count
                
            if tailCount == 5:
                streakTail += 1
                tailCount = 0          #Reinitialize streak count
                
        else:  #Reinitialize streak count
            headCount = 0
            tailCount = 0

    # test code manually
    if number == 0:
        print()
        print('Test code:')
        print(coinList)
        print()
        print('streakTail: ',streakTail, '; streakHead: ', streakHead)
        print()

# Total number of streak 
totalStreak = streakHead + streakTail

# Print result 
print('In 10000 coins flip, here is the result:', end='\n ')
print('Number of streak of six heads: ',streakHead, end='\n ')
print('Number of streak of six tails: ', streakTail, end='\n ')
print('The percentage of coins flip that contains a streak of six heads or tails in a row is: ', round((totalStreak/(100*10000/6))*100,2),'%')

    
