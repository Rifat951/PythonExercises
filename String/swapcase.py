

user_input=input("Enter String : \n")

count = 1

user_list = ' '


for user_list in user_input:
   # print(user_input[count],end = '')
    count = count +1
    if count % 2 == 0:
        var_1 = user_list.upper()
    else:
       var_2 = user_list.lower()
       var = var_1 + var_2
       print("{}".format(var),end='')

       