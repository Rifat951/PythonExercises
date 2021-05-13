# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders Make sure no pastrami sandwiches end up
# in finished_sandwiches



acitve_loop = True

ingredients = []
finished_sandwich = []

while acitve_loop:
    san_ing = input("Enter Ingredients : ")

    if san_ing == "quit":
        break
    else:
        ingredients.append(san_ing)

print(ingredients)

while ingredients:
    # use the list (ingredients) instead of flag
    current_sandwich = ingredients.pop()
    ##print("Sorry we have run out of Pastrami")
    finished_sandwich.append(current_sandwich)



while 'pastrami' in finished_sandwich:
    finished_sandwich.remove('pastrami')
    print("sorry we have run out of pastrami\n")

for lists in finished_sandwich:
    print("\nSandwich left is {}".format(lists))
