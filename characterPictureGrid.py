# Character Picture Grid: this program uses a grid of character to print a given image

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

row = 9
column = 6

for x in range(row):
    if x == 0:
        for y in range(column):
            if y == 1:
                print(2*grid[x][y], sep='', end='')
                break
    
    if x == 1:
        for y in range(column):
            if y == 1:
                print(2*grid[x][y], sep='', end='')
            if y == 3:
                print(grid[x][y], sep='', end='')
                break
    if x == 2:
        for y in range(column):
            if y == 0:
                print(2*grid[x][y], sep='', end='')
            if y == 4:
                print(2*grid[x][y], sep='', end='')
                print() # end of first line

            if y == 5:
                print(grid[x][y], sep='', end='')
                break 
    if x == 3:
        for y in range(column):
            if y == 1:
                print(7*grid[x][y], sep='', end='')
            if y == 5:
                print(grid[x][y], sep='', end='')
                print() # end of second line
                print(grid[x][y], sep='', end='')
                
        for y in range(column):
            if y == 1:
                print(7*grid[x][y], sep='', end='')
            if y == 5:
                print(grid[x][y], sep='', end='')
                print() # end of third line
                break
    if x == 4:
        for y in range(column):
            if y == 0:
                print(2*grid[x][y], sep='', end='')
            if y == 1:
                print(5*grid[x][y], sep='', end='')
                break
    if x == 5:
        for y in range(column):
            if y == 5:
                print(2*grid[x][y], sep='', end='')
                print() # end of fourth line
                break


    if x == 6:
        for y in range(column):
            if y == 4:
                print(3*grid[x][y], sep='', end='')
                break
    if x == 7:
        for y in range(column):
            if y == 1:
                print(3*grid[x][y], sep='', end='')
            if y == 3:
                print(3*grid[x][y], sep='', end='')
                print() # end of fifth line
        
        for y in range(column):
            if y == 0:
                print(4*grid[x][y], sep='', end='')
            if y == 1:
                print(grid[x][y], sep='', end='')
                break
    if x == 8:
        for y in range(column):
            if y == 0:
                print(4*grid[x][y], sep='', end='')
                print() # end of sith line
               
            
        
                
        
                
        
                
                
            
    
                
        
                         

        
        
               
    
