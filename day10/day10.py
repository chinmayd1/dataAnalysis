
# Day 10 Numpy Arrays Vs Python Lists

#import numpy as np
#from numpy import *
#import numpy
#from numpy import array


import numpy as np 
listA = [1,2,3,4,5]
arr1 = np.array([1,2,3,4,5])
print(type(listA)) # list
print(type(arr1)) # numpyArray

print(listA * 2)
print(arr1 * 2)

# Arithimetic operations using numpy array 
arr2 = np.array([10,20,30,40,50])
print("array - addition",arr2+2)
print("array - subtraction",arr2-2)
print("array - multiplication",arr2*2)
print("array - division",arr2/2)

# How it is faster?
# Arrays Creation Functions

# range(startIndex,endIndex(not included),stepSize)

arr2 = np.array([1,2,3,4,5])
print(np.zeros(5))
print(np.ones(4))
print(np.arange(2,11,2))
print(np.arange(3,31,3))
print(np.linspace(5,10,10))

# [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]

# ]
print(np.arange(1,11,1).reshape(2,5)) # row, column
print(np.arange(1,11,1).reshape(5,2)) # row column


