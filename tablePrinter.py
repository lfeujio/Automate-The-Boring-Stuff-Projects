# This is the Table printer program: this is a function that takes a list of lists of strrings and displays it in a well-organized table with each column right-justified. 


# Function definition

def printTable(listOfList):

    rowWidth = len(listOfList)
    columnWidth= [0]*len(listOfList)

    for i in range(len(listOfList)):
        columnWidth[i] = len(listOfList[i])

    # Formatting of the table
    for x in range(len(columnWidth)):
        for i in range(columnWidth[x]):
            for j in range(rowWidth):
                print(listOfList[j][i].rjust(10), end = '')
            print()
        break
        

# Test function

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['loic', 'feujio', 'tenandjo', '1992'],
             ['the', 'cover', 'smart', 'python']]

printTable(tableData)
