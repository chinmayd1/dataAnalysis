from array import *
# 23,4,5,6,7,8---> split()---->[4,5,6,7,8]
# from list create array 
# loop --> total 
# mark/total * 100 -- percentage
# "4,5,6,7,8"            ["4","5","6","7","8"]
#listS  = input('Enter the marks ').split(',')

# listI = [int(x) for x in input('Enter the marks ').split(',')]
# # [4,5,6,7,8]
# marks = array('i',listI)
# sum = 0
# for x in marks:
#     sum = sum + x
# print(f"The total marks are :{sum}")
# print((sum/50)* 100)

# program 2
# sequential search ---> 5 element 
# position of particular 
# element will stored in array 
# identify the posisition for array 



a = array('i',[])
numberOfValues = int(input("how many values you wish to enter:"))#5
for x in range(numberOfValues):
    e = int(input("enter a number :"))
    a.append(e)
print(a)
fe = int(input('Enter the element you wish to search'))
flag = False
for x in range(len(a)):
    if a[x] == fe:
        flag = True
        print(f"The position for the element is:{x+1}")

if  flag == False:
    print("unable to find element ...")
