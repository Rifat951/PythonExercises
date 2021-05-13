# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a different
# message

def make_shirt(size,text):
    # print("{} is the size".format(size))
    # print("{} should be printed on the shirt".format(text))
    if size == "large":
        print("{} is the shirt size ".format(size))
        print("I love python".format(text))
    elif size == "medium":
        print("{} is the shirt size ".format(size))
        print("this is available".format(text))
    else:
        print("{} is the shirt size ".format(size))
        print("Write down anything you want".format(text))


number = input("Enter the size of shirt... \n")
text_shirt = " "

make_shirt(number,text_shirt)