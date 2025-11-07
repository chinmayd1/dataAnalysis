# Boolean indexing 
#import numpy
import numpy as np
# from numpy import *
# from numpy import array

# boolean indexing 
# fancy indexing


arr = np.array([10,20,30,40,50,60,70])
bool_mask = arr > 40   # [False,False,False,False,True,True,True]
filterArray = arr[bool_mask]
print(filterArray)


# Boolean masking applying various condition 
arr = np.array([10,20,30,40,50,60,70])
e = arr[(arr > 20) & (arr < 60)] # elements between 20 and 60
print(e)
e2 = arr[(arr < 30) | (arr > 60)]  # less than 30 and greater than 60
print(e2)
print(arr[~(arr > 40)]) # Not greater than 40

# Boolean indexing on 2D array 
mat = np.array([
    [10,25,30],
    [40,50,60],
    [70,85,90]
])
# flatten and filter operation in one step
# extract all the elements greater than 50
e7 = mat[mat > 50]
print(e7)

arr = np.array([10,20,30,40,50,60,70])
e8 = arr[arr > 50] = 99
print(e8)


#  FANCY ----------------------> INDEXDING
#               0  1  2  3  4  5  6
arr = np.array([10,20,30,40,50,60,70])
print(arr[[0,2,4]])


# first and last row
mat = np.array([
    [10,25,30],
    [40,50,60],
    [70,85,90]
])

print(mat[[0,-1]])