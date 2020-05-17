# create a 6x6 matrix

import random

width = 6
height = 6

matrix = []

for x in range(width):

    newColumn = []

    for y in range(height):
        if random.randint(0,1)== 1:
            newColumn.append('#')
        else:
            newColumn.append('@')

    matrix.append(newColumn)

# print matrix

for y in range(height):

    for x in range(width):
        print(matrix[x][y], end='')
    print()

