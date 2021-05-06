# 5-10. Checking Usernames: Do the following to create a program that simulates
# how websites ensure that everyone has a unique username
# •	 Make a list of five or more usernames called current_users
# •	 Make another list of five usernames called new_users Make sure one or
# two of the new usernames are also in the current_users list
# •	 Loop through the new_users list to see if each new username has already
# been used If it has, print a message that the person will need to enter a
# new username If a username has not been used, print a message saying
# that the username is available • Make sure your comparison is case insensitive If 'John' has been used,
# 'JOHN' should not be accepted



old_user = []
user_input = int(input("Enter user count : "))

for users in range(user_input):
    user_name = input("Enter name : ")
    old_user.append(user_name)

for user in old_user:
    print(user, end= " ")

new_user = []
new_user_input = int(input("\nEnter user count for new user : "))

for new_users in range(new_user_input):
    new_user_name = input("Enter name : ")
    new_user.append(new_user_name)

for newuser in new_user:
    print(newuser, end= " ")

print("\n")
#iterate multiple list

for new,old in zip(new_user, old_user):
    if new_user == old_user:
        if new.upper() == new:
            print("Failed case")
        else:
            print("Value need to be replaced")
            replaced_user = input("Enter replaced Name : ")
            new_user.append(replaced_user)
    else:
        print("Name is available")
