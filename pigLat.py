# This program transforms a sentence in a made up language:  If a word begins with a vowel, the word yay is added to the end of it.
# If a word begins with a consonant or consonant cluster (like ch or gr), that consonant or cluster is moved to the end of the word followed by ay.


print('Enter the english sentence to translate in Pig Latin')
message = input()

messageToList = message.split()
print(messageToList)
print()

vowelList = ['a','e','i','o','u','y']
answer = False

for x in range(len(messageToList)):
    if messageToList[x].isalpha():

         for vowel in vowelList:
             if (messageToList[x].lower()).startswith(vowel):
                 answer = True
                 print(messageToList[x])
                 break
                 
         if answer == True:
             
             if messageToList[x].islower():
        
                 messageToList[x] = messageToList[x] + 'yay'
                 answer = False
                 
             elif messageToList[x].isupper():
                 messageToList[x] = messageToList[x] + 'YAY'
                 answer = False
             else:
                 messageToList[x] = messageToList[x] + 'yay'
                 answer = False
                 
                    
         else:


             if messageToList[x].islower():
                 wordToList = list(messageToList[x])         # create a list from individual word to be able to move them around
                 wordToList.append(wordToList[0])   # Add first letter at the end of the list
                 wordToList = wordToList[1:]        # Delete the first letter
                 newWord = ''.join(wordToList)     # Turn the list into a string
                 newWord = newWord + 'ay'           # Add 'ay' at the end of the word
                 messageToList[x] = newWord                     # Assign the new language word to the previous one
                 
             elif messageToList[x].isupper():
                 wordToList = list(messageToList[x])         # create a list from individual word to be able to move them around
                 wordToList.append(wordToList[0])   # Add first letter at the end of the list
                 wordToList = wordToList[1:]        # Delete the first letter
                 newWord = ''.join(wordToList)     # Turn the list into a string
                 newWord = newWord + 'AY'           # Add 'ay' at the end of the word
                 messageToList[x] = newWord                     # Assign the new language word to the previous one

             else:
                 wordToList = list(messageToList[x])         # create a list from individual word to be able to move them around

                 wordToList.append(wordToList[0].lower())
                 wordToList = wordToList[1:]        # Delete the first letter
                 wordToList[0] = wordToList[0].upper()
                  
                 newWord = ''.join(wordToList)     # Turn the list into a string
                 newWord = newWord + 'ay'           # Add 'ay' at the end of the word
                 messageToList[x] = newWord                     # Assign the new language word to the previous one
                  








                  
            
             
             

newMessage = ' '.join(messageToList)

print()
print(newMessage)

                
    
