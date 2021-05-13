# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15 Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket


loop_flag = True

while loop_flag:
    input_age = int(input("Enter the age : \n"))
    if 0 <= input_age < 3:
        print("go home")
    elif 3 <= input_age <= 12:
        print("Ticket value is $10")
        break
    else:
        print("Ticket Value is $15")
        break
