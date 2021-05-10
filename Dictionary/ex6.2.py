# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers
# Think of five names, and use them as keys in your dictionary Think of a favorite
# number for each person, and store each as a value in your dictionary Print
# each person’s name and their favorite number For even more fun, poll a few
# friends and get some actual data for your program

print("\n\n")
print("####################")
print("\n\n")
user_numbers = {
    'first_user': 213141,
    'second_user': 2441139,
    'third_user': 700,
    'fourth_user': 200021,
    'fifth_user': 201912,
 }

for user_id, user_num in user_numbers.items():
    print("{} : {}".format(user_id,user_num))