#COMA CODE: This function takes a list value as an argument and returns a string with all the items separated by a comma a space, with and inserted before the last item

import sys

def comma(fnList):

    try:
        str1 = ""

        for item in fnList[:-1]:
            str1 += item + ', '
        

        print(str1, 'and', fnList[-1])

    except IndexError:

        print()
        print('This is an empty list')
        sys.exit()


spam = ['apples', 'bananas', 'tofu', 'cats', 'oranges']

spam2 = []

comma(spam)
comma(spam2)
