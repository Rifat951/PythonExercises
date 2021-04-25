# 4-1. Pizzas: Think of at least three kinds of your favorite pizza Store these
# pizza names in a list, and then use a for loop to print the name of each pizza
# •	 Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza
# •	 Add a line at the end of your program, outside the for loop, that states
# how much you like pizza The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!

print("###################################")

pizz_menu = []

input_number_of_flavour = int(input("Enter Number of Flavours : "))


for numbers in range(input_number_of_flavour):
    pizza_details = input("Flavour :")
    print("I love {}".format(pizza_details))
    pizz_menu.append(pizza_details) # will add pizza element
# print("I love these pizzas "+str(pizz_menu))
print("Love for {} pizza is eternal ")



# 4-2. Animals: Think of at least three different animals that have a common characteristic Store the names of these animals in a list, and then use a for loop to
# print out the name of each animal
# •	 Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# •	 Add a line at the end of your program stating what these animals have in
# common You could print a sentence such as Any of these animals would
# make a great pet!

print("\n\n\n")
print("#############################################")
pet_animal = []

InputPetNames = int(input("Enter Pet Count : "))

for PetName in range(InputPetNames):
    PrintPetName = input("Enter Pet Names : ")
    if PrintPetName == "dog":
        print("{} would make a good pet".format(PrintPetName))
    elif PrintPetName == "cat":
        print("{} can stay in couch".format(PrintPetName))
    else:
        print("error")

print("Any of them would make great pet")
