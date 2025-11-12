# Aggregate functions 

import numpy as np 
arr = np.array([10,20,30,40,50])
print("Sum",np.sum(arr))

# program 2

mat = np.array([
    [1,2,3],
    [4,5,6]
])
print(np.sum(mat))

# Sum by row 
row = np.sum(mat,axis=1)
print(row)

# Sum by colum 
cols = np.sum(mat,axis=0)
print(cols)

# program 2
# mean 

arr2 = np.array([10,20,30,40])
print(np.mean(arr2))

mat = np.array([
    [1,2,3],
    [4,5,6]
])

col  = meanCol = np.mean(mat,axis=0)
row = meanRow = np.mean(mat,axis=1)
print(col)
print(row)

# median 
arr = np.array([10,20,30,40,50])
print(np.median(arr))


arr = np.array([10,20,30,40,50])
print(np.min(arr))
print(np.max(arr))

mat = np.array([
    [1,2,3],
    [4,5,6]
])

print(np.min(mat,axis=0))
print(np.min(mat,axis=1))
print(np.max(mat,axis=0))
print(np.max(mat,axis=1))

# standard deviation
#print(sum([60,70,80,90,100])/5)
#print(sum([10,15,20,5,350])/5)
#((10-80)**2 + (15 - 80)**2+ (20-80)**2+(5-80)**2+(350-80)*2)/5
#std ---> sqrt(var)

arr = np.array([10,15,20,5,350])
print(np.var(arr))
print(np.std(arr))