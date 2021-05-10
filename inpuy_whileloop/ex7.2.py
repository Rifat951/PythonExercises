# 7-2. Restaurant Seating: Write a program that asks the user how many people
# are in their dinner group If the answer is more than eight, print a message saying they’ll have to wait for a table Otherwise, report that their table is ready

print("Enter the user count \n")
table_count = int(input())

if table_count >= 8:
    print("Please wait for a while")
else:
    print("please dine in")
