# Exercise 3: Print characters from a string that are present at an even index number

# Write a program to accept a string from the user and display characters that are present at an even index number.

# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’



# declare a string
# turn it into a list
# find the index of the list
# print out even numbers ranging from 0, 2, 4


name = "pynative"

strToList = list(name)
# lengthList = len(strToList)

# getting length of list
length = len(strToList)
  
# Iterating the index
# same as 'for i in range(len(list))'
for i in range(length):
    if( i % 2 == 0):
         print(strToList[i])
# print(strToList)
