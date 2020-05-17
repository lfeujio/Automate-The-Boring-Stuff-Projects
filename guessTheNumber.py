# This is a guess a number game

import sys, random

numberGuess = 0

print('I am thinking of a number between 1 and 20.')
number = random.randint(1,20)

while True:
    
    print('Take a guess.')
    guess = int(input())
    numberGuess = numberGuess + 1
          
    if guess < number:
        print('Your guess is too low.')
        continue
    
    elif guess > number:
        print('Your guess is too high.')
        continue
    
    else:
        print('Good job! You guessed my number in ' + str(numberGuess) + ' guesses!')
        sys.exit()
    
        
     
    
