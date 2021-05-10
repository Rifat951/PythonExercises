# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values
# When you’re sure that your loop works, add five more Python terms to your
# glossary When you run your program again, these new words and meanings
# should automatically be included in the output

print("\n\n")
print("####################")
print("\n\n")
glossary = {
    'If-else': "represents conditional statements",
    'loop': "write the statement without copy and pasting it everytime... tadaaa!",
    'variable_1' : "declare variable_1",
    'variable_2' : "declare variable_2",
    'variable_3' : "declare variable_3"
 }

for user_key, user_val in glossary.items():
    print("{} ".format(user_key))
    # print("\n")
    print("{}".format(user_val))
    print("\n")