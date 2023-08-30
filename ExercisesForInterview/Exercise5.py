# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

# Given list: [10, 20, 30, 40, 10]
# result is True

# numbers_y = [75, 65, 35, 75, 30]
# result is False



def TF(listofNum):
    
        if(listofNum[0] == listofNum[-1]):
            print("True")
        else:
            print("False")



listt =  [75, 65, 35, 75, 30]
TF(listt)
