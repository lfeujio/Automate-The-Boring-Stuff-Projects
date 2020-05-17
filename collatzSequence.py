# This program print the quotient of the division of a number by 2 if that number is even, and multiply that number by 3 and add 1 if that number is odd

import sys

result = 0     # global variable to hold the results of function collatz

def collatz(number):
    global result
    
    if (number%2) == 0:
        print(str(number//2))
        result = number//2
        return result
        
        
    else:
        print(str(3*number + 1))
        result = 3*number + 1
        return result 
        
    

# Ask user to enter a number
print('Enter a number:')


try:
    userNumber = int(input())

except ValueError:
    print('Please enter a number not a string:')
    userNumber = int(input())

# First call of the collatz sequence using user input
collatz(userNumber)

# Keep calling the collatz sequence with the result of the previous call

while True:

    if result == 1:
        sys.exit()
    else:
        collatz(result)
