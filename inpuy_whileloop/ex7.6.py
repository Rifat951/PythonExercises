# 7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
# that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop
# •	 Use an active variable to control how long the loop runs
# •	 Use a break statement to exit the loop when the user enters a 'quit' value



loop_flag = True

pizza = []

while loop_flag:
    pizza_topping = input("Enter pizza topping : \n")
    if pizza_topping == "quit":
        print("Code has stopped working....")
        break
    else:
        print("Continue adding toppings... \n")
        pizza.append(pizza_topping)

print("\n")
for ingredients in pizza:
    print(ingredients,end=" ")