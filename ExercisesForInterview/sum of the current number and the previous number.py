summ = 0
previousNum = 0

for i in range (10-1):
    if(previousNum == i):
        print("previousNum", previousNum, "Next",i, "summ", summ)
    if( previousNum  != i +1):
        summ = i +(i+1)
        print("previousNum", i, "Next",i+1, "summ", summ)
        #print("Next",i+1)
        # print(summ)





# previousNum 0 Next 0 summ 0
# previousNum 0 Next 1 summ 1


# previousNum 1 Next 2 summ 3


# previousNum 2 Next 3 summ 5


# previousNum 3 Next 4 summ 7


# previousNum 4 Next 5 summ 9


# previousNum 5 Next 6 summ 11


# previousNum 6 Next 7 summ 13


# previousNum 7 Next 8 summ 15


# previousNum 8 Next 9 summ 17
