# 6-6. Polling: Use the code in favorite_languages.py (page 104)
# •	 Make a list of people who should take the favorite languages poll Include
# some names that are already in the dictionary and some that are not
# •	 Loop through the list of people who should take the poll If they have
# already taken the poll, print a message thanking them for responding
# If they have not yet taken the poll, print a message inviting them to take
# the poll


print("\n\n")
print("####################")
print("\n\n")

language = {
    'rafi': 'c',
    'tafi': 'python'
 }
poll_list = {
   "rafi": 1,
   "tafi": 2,
   "shironeko": 3
 }

for user_key, usr_val in poll_list.items():
    if 1 <= usr_val <= 2: #simple chain condition
        print("{} Thanks for using the poll".format(user_key))
    else:
        print("{} Please do the poll again".format(user_key))
