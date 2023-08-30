# Exercise 6: Display numbers divisible by 5 from a list

# Iterate the given list of numbers and print only those numbers which are divisible by 5

# Expected Output:

# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55


def divNum(listNumber):
    for i in (listNumber):
        if( i % 5 == 0):
            print(i)

listNum = [10, 20, 33, 46, 55]
divNum(listNum)
