#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip
text = pyperclip.paste()

print(text)
print()
# Separate lines and add stars.
lines = text.split('\n')

print(lines)
print()
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
    print(lines[i])
          
text = '\n'.join(lines)

print()
print(text)
          
pyperclip.copy(text)
