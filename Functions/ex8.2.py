# 8-2. Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title The function should print a message, such as One of my
# favorite books is Alice in Wonderland Call the function, making sure to
# include a book title as an argument in the function call

def favourite_book(book_name):
    print("My favourite book is {}".format(book_name))

book_data = input("Enter name of the book : \n")

favourite_book(book_data)
