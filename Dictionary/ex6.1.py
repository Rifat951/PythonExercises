# 6-1. Person: Use a dictionary to store information about a person you know
# Store their first name, last name, age, and the city in which they live You
# should have keys such as first_name, last_name, age, and city Print each
# piece of information stored in your dictionary

print("\n\n")
print("####################")
print("\n\n")

user_info = {
    'first_name': 'rafi',
    'last_name': 'tafi',
    'User_Age': 18,
    'City': 'You do not need to know'
    }

for user_key, user_value in user_info.items():
    print("{} : {}".format(user_key,user_value))
