
# universal functions 
# mathematics , trignometric , statistical ufunctions 
# to array

# addition ,subtraction , multiplication 
# division , power , remainder

import numpy as np 
arr1 = np.array([10,20,30,40])
arr2 = np.array([1,2,3,4])
print(np.add(arr1,arr2))
print(np.subtract(arr1,arr2))
print(np.multiply(arr1,arr2))
print(np.divide(arr1,arr2))
print(np.mod(arr1,3))


# program 2
arr = np.array([1,4,9,16,25])
print(np.sqrt(arr))
arr2 = np.square([1,4,9,16,25])
print(arr2)
print(np.exp(arr))
print(np.log(arr))

#Rounding off and absolute values
# Ceiling , Floor , Round , Absolute

arr = np.array([3.14,2.67,-5.89,45.67])
print(np.ceil(arr))

arr2 = np.array([3.14,2.67,-5.89,45.67])
print(np.floor(arr2))

arr2 = np.array([3.14,2.67,-5.89,45.46])
print(np.round(arr2,1))

arr2 = np.array([3.14,2.67,-5.89,45.46])
print(np.abs(arr2))



