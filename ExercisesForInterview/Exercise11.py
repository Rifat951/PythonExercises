# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.

# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.


# num  = 7536
# intTostr = str(num)[::-1]
# print(intTostr, end = " ")



number = 7536
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")
