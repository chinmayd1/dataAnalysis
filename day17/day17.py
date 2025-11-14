
# Sorting , Searching  & Counting (Detailed)

# Sorting Arrays
import numpy as np 
e = np.array([25,10,15,5,40])
e2 = np.sort(e)
print(e)
print(e2)

# 2D array sorting 

mat = np.array([
    [3,2,11],
    [7,9,8]
])
#[1,2,3]
#[7,8,9]
print(np.sort(mat,axis = 1)) # row wise sorting 
print(np.sort(mat,axis = 0)) # column wise sorting


# program 3
# np.argsort()

#               0  1   2  3  4
arr = np.array([50,60,10,80,20])
arr2 = np.array([50,60,100,80,20])
indices = np.argsort(arr)
print(indices)
print(arr[indices])
print(arr2[indices])

# Searching with conditions 

arr = np.array([10,20,30,40,50,60])
idx = np.where(arr > 30)
print(idx)
print(arr[idx])


# conditional statement using np.where 
arr = np.array([10,20,30,44,56,78,66])
result = np.where(arr > 60,"Pass","Fail")
print(result)

# search sorted arrays 
arr = np.array([10,20,30,44,56,78,66])
arr2 = np.searchsorted(arr,35)
print(arr2)

# counting non zeros 
arr = np.array([44,56,0,78,66,0])
print(np.count_nonzero(arr))

# any 
print(np.any(arr > 70))
# all
print(np.all(arr > -1))

# Unique values and frequency 

arr = np.array([1,2,3,2,3,4,6,5])

value,counts = np.unique(arr,return_counts = True)
print(value)
print(counts)
