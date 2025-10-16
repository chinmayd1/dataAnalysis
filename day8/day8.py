# pip install numpy
# creating
# single dimensional array

import numpy 
e1 = numpy.array([10,12,3,44,55,66])

import numpy as np 
e2 = np.array([12,33,4,4,5])

from numpy import *
e3 = array([33,44,55,66,77])

# character
e4 = array(['a','b','c','d'])

e5 = ["pune","mumbai","banglore","kolkata","chennai"]
print(e5)

print(e1)
print(e2)
print(e3)
print(e4)

# creating a array from another array 
q = array([11,22,33,44])
q2 = array(q)
print(q)
print(q2)

# arange(start,stop(not included),stepsize)
q3 = arange(2,21,2)
print(q3)

q4 = arange(50,0,-5)
print(q4)

q5 = arange(10,0,-1)
print(q5)

# program 2

# by default float
q6 = zeros(5)
print(q6)

q7 = zeros(5,int)
print(q7)

q8 = ones(5)
q9 = ones(5,int)
print(q8)
print(q9)


# program 3
d = [11,22,33,44]
add10 = []
for x in d:
    add10.append(x+10)
print(add10)

d2 = array(d) + 10
print(d2)
print(type(d2))