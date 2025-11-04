import numpy as np 
a = np.zeros(5,dtype=int)
print(a)

# 2D using numpy
a1  = np.zeros((3,3),dtype=int) # rows # columns
print(a1)

a3 = np.ones(5,dtype=int)
print(a3)

a4 = np.ones((2,3),dtype=int)
print(a4)

# program 2 
# arange(0,10,1)
a4 = np.arange(10)
a5 = np.arange(2,21,2).reshape(5,2)
print(a5)

a6 = np.linspace(0,10,5)
print(a6)
a7 = np.linspace(0,1,10)
print(a7)

# program 3
a8  = np.eye(4,dtype=int)
print(a8)

# program 4
a9 = np.full((2,3),7)
print(a9)

# Accessing the element from 1 day 

a10 = np.array([10,20,30,40,50])
print(a10[0])
print(a10[1])
print(a10[2])
print(a10[3])
print(a10[4])

print(a10[-1])
print(a10[-2])
print(a10[-3])

a11 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(a11[0,2])
print(a11[2,2])

# [     0 1 2
#     0[1,2,3],
#     1[4,5,6],
#     2[7,8,9]
# ]


# 6 pm , 6:30 pm , 7:30 pm , 8 pm javascript , 8:30 pm
# 8:30 am   - prompt engineering
# Power BI