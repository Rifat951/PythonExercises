# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary
# However, to avoid confusion, let’s call it a glossary
# •	 Think of five programming words you’ve learned about in the previous
# chapters Use these words as the keys in your glossary, and store their
# meanings as values
# •	 Print each word and its meaning as neatly formatted output You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output


print("\n\n")
print("####################")
print("\n\n")
glossary = {
    'If-else': "represents conditional statements",
    'loop': "write the statement without copy and pasting it everytime... tadaaa!"
 }

for user_key, user_val in glossary.items():
    print("{} ".format(user_key))
    # print("\n")
    print("{}".format(user_val))
    print("\n")
