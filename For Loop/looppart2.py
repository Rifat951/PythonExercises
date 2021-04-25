# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive


#
disp_numbers = [value for value in range(1,21)]
print(disp_numbers)
#
#
# # 4-4. One Million: Make a list of the numbers from one to one million, and then
# # use a for loop to print the numbers (If the output is taking too long, stop it by
# # pressing ctrl-C or by closing the output window )
#
for num in range(1,1000000):
    print(num)

#
# # 4-5. Summing a Million: Make a list of the numbers from one to one million,
# # and then use min() and max() to make sure your list actually starts at one and
# # ends at one million Also, use the sum() function to see how quickly Python can
# # add a million numbers
#
empt_lst = []
for num in range(1,100000):
    empt_lst.append(num)

print("{} is minimum value ".format(min(empt_lst)))
print("{} is minimum value ".format(max(empt_lst)))
print("{} is minimum value ".format(sum(empt_lst)))


# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20 Use a for loop to print each number


odd_number = [ValueofOddNumbers for ValueofOddNumbers in range(1,20,2)]
print(odd_number)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30 Use a for loop to
# print the numbers in your list

#approach 1
cube = [NumberCube*3 for NumberCube in range(3,30)]
print(cube)

#approach 2
cubical = []
for cubic in range(3,30):
    cubical.append(cubic*3)
print(cubical)


# 4-8. Cubes: A number raised to the third power is called a cube For example,
# the cube of 2 is written as 2**3 in Python Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube

print("\n###########################")
cube_without_comp = []
for CubeTest in range(1,10):
    cube_without_comp.append(CubeTest**3)
print(cube_without_comp)


# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes


cubics = [cub**3 for cub in range(1,10)]
print("with list comprehension {} ".format(cubics))