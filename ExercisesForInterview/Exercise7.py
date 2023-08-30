# Exercise 7: Return the count of a given substring from a string

# Write a program to find how many times substring “Emma” appears in the given string.





def countStr(string):
    retString = string.count("Emma")
    print(retString)

str_x = "Emma is good developer. Emma is a writer"
countStr(str_x)
