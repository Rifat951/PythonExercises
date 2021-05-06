# 5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
# not empty
# •	 If the list is empty, print the message We need to find some users!
# •	 Remove all of the usernames from your list, and make sure the correct
# message is printed

user_name = []
input_username_count = int(input("Enter How many users : "))

for user in range(input_username_count):
    nameofuser = input("Input User Name : ")
    user_name.append(nameofuser)
print("\n")
for users in user_name:
    if users  == 'admin':
        print("Helloo to the admin panel... {}".format(users))
    else:
        print("Welcome to interface {}".format(users))

print("\n")
user_name.clear() ## removes all the values from list
if not user_name:
    print("Empty list...")