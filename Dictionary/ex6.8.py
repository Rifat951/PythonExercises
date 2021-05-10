# 6-8. Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet In each dictionary, include the kind of animal and the owner’s
# name Store these dictionaries in a list called pets Next, loop through your list
# and as you do print everything you know about each pet


print("\n\n")
print("####################")
print("\n\n")

user_info = {
    'pet' : 'doggo',
    'owner' : 'rafi',
    'store' : 'unknown'
    }

user_info_2 = {
    'pet' : 'catto',
    'owner' : 'pafi',
    'store' : 'unknown'
    }
for user_details in [user_info,user_info_2]:
    print("\n")
    print(user_details)