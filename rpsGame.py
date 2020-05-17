# This is the Rock Paper Scissors Game

import random, sys

Wins = 0
Losses = 0
Ties = 0
rps_list = ['ROCK','PAPER','SCISSORS']

print('ROCK, PAPER, SCISSORS')

while True:
    
    print('')                          #space the text printed on the screen
    print(str(Wins) + ' Wins,' + str(Losses) + ' Losses,' + str(Ties) + ' Ties')
    print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
    
    machineMove = random.choice(rps_list)
    yourMove = input()

    if yourMove == 's':
        yourMove = 'SCISSORS'
    elif yourMove == 'r':
        yourMove = 'ROCK'
    elif yourMove == 'p':
        yourMove = 'PAPER'
    
    elif yourMove == 'q':
        yourMove = 'quit'
    else:
        print('Error: only enter r,p,s,q')
        continue
        
    if yourMove == machineMove:
        print(yourMove + ' versus...')
        print(machineMove)
        print('It is a tie!')
        Ties = Ties + 1
        continue
    
    else:
        if yourMove == 'ROCK':
            print(yourMove + ' versus...')
            print(machineMove)
            
            if machineMove == 'PAPER':
                print('You lose!')
                Losses = Losses + 1
            else:
                print('You win!')
                Wins = Wins + 1
            continue
        
        elif yourMove == 'SCISSORS':
            print(yourMove + ' versus...')
            print(machineMove)
            
            if machineMove == 'ROCK':
                print('You lose!')
                Losses = Losses + 1
            else:
                print('You win!')
                Wins = Wins + 1
            continue
        
        elif yourMove == 'PAPER':
            print(yourMove + ' versus...')
            print(machineMove)
            
            if machineMove == 'SCISSORS':
                print('You lose!')
                Losses = Losses + 1
            else:
                print('You win!')
                Wins = Wins + 1
            continue
        
        
        else:
            sys.exit()

     
            
            
        
    


