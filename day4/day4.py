# similar type of data 
info = ["chinmay","deshpande",12,True]

#array willl have same set of data

# import array 
# arrOne  = array.array('i',[5,6,7,8,9])
# for element in arrOne:
#     print(element)


# program 2
from array import *
q2 = array('u',['a','b','c','d'])
print(q2)
for element in q2:
    print(element)

# program 3
from array import *
arr1 = array('d',[1.5,2.5,3.5])

#(a * 2 for x in arr1)
#arr2 = array('d',(x * 2 for x in arr1))
arr2 = array(arr1.typecode,(x * 2 for x in arr1))
print(arr2)

# program 4

arr3 = array('i',[11,222,33,44,55,66])
print(len(arr3))
for x in range(len(arr3)):
    #print(x)
    print(arr3[x])


# program 5
i2  = 0
while(i2 < len(arr3)):
    print(i2)
    print(arr3[i2])
    i2 = i2 + 1

# program 6