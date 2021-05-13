# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value As they enter each topping,
# print a message saying you’ll add that topping to their pizza



loop_flag = True

pizza = []

while loop_flag:
    pizza_topping = input("Enter pizza topping : \n")
    if pizza_topping == "quit":
        loop_flag = False
        print("Code has stopped working....")
    else:
        print("Continue adding toppings... \n")
        pizza.append(pizza_topping)

print("\n")
for ingredients in pizza:
    print(ingredients,end=" ")
