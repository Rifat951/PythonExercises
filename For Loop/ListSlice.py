
# 4-10. Slices: Using one of the programs you wrote in this chapter, add several
# lines to the end of the program that do the following:
# •	 Print the message, The first three items in the list are: Then use a slice to
# print the first three items from that program’s list
# •	 Print the message, Three items from the middle of the list are: Use a slice
# to print three items from the middle of the list
# •	 Print the message, The last three items in the list are: Use a slice to print
# the last three items in the list
#
donut_list = []
donut_inp = int(input("Enter the count of donuts: \n"))


for dount_count in range(donut_inp):
    donut_details = input("Donut types: \n")
    donut_list.append(donut_details)

for donut_number in donut_list:
    print("Details of Donuts: {} ".format(donut_number,end=" "))
print("\n")
for donut_slice in donut_list[:3]:
    print("Sliced donuts first three items {}".format(donut_slice,end =" "))
print("\n")
for donut_slice in donut_list[2:5]:
    print("Sliced donuts middle three items {}".format(donut_slice,end =" "))

print("\n")

for donut_slice in donut_list[-3:]: # -3 will be counted from backwards. For and example 1-7.... 7 will be -1, 6 will be -2, 5 will be -3
    print("Sliced donuts last three items {}".format(donut_slice,end =" "))

# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
# (page 60) Make a copy of the list of pizzas, and call it friend_pizzas
# Then, do the following:
# •	 Add a new pizza to the original list
# •	 Add a different pizza to the list friend_pizzas
# •	 Prove that you have two separate lists Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second list Make sure each new pizza is stored in the appropriate list

pizza_list = []
input_pizza_count = int(input("Pizza count : \n"))

for number_pizza in range(input_pizza_count):
    pizza_type = input("Enter pizza type : \n")
    pizza_list.append(pizza_type)
print("My Pizza List {} ".format(pizza_list))

friend_pizza_list = pizza_list[:] #basically [:] means we will copy from the first and last element of this whole pizza_list
print("Pizza list of Friend : {} \n".format(friend_pizza_list))

pizza_list.insert(1, "the work by pizzahut")
friend_pizza_list.insert(2, "Delicacy")

print("My new Pizza List {} \n".format(pizza_list))
print("\nNew Pizza list of Friend : {} ".format(friend_pizza_list))



# 4-12. More Loops: All versions of foods.py in this section have avoided using
# for loops when printing to save space Choose a version of foods.py, and
# write two for loops to print each list of foods

food_list = []
input_value_of_count = int(input("enter count : \n"))

for food_count in range(input_value_of_count):
    food = input("enter food detail :\n")
    food_list.append(food) # food will get append with food_list.... otherwise input value will not be displayed
print(food_list)

for food_slice in food_list:
    print(food_slice,end=' ')

