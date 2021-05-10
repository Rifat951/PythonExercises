# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 102)
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people Loop through your list of people As you
# loop through the list, print everything you know about each personDictionaries 115


import  pprint

print("\n\n")
print("####################")
print("\n\n")


appended_list = {"new_list": []}

user_info = {
    'first_name': 'rafi',
    'last_name': 'tafi',
    'User_Age': 18,
    'City': 'You do not need to know'
    }

user_info_2 = {
    'first_name': 'luffy',
    'last_name': 'Monkey D.',
    'User_Age': 20,
    'City': 'Grandline'
    }
for user_details in [user_info,user_info_2]:
    print("\n")
    appended_list['new_list'].append(user_details)



pretty_print = pprint.PrettyPrinter()
pretty_print.pprint(appended_list)

###pretty printer has issues... it displays in alphabetic order....



