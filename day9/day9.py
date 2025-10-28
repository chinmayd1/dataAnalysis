

# Explain what is numpy ?
# install and import numpy 
# creating numpy arrays 
# understanding difference between list and numpy arrays
# basic  attributes and methods 

# [1,2,3,4,5]
# ["chinmay","deshpand",44,66]
# int , float , string , boolean


# why numpy ?
# python libraby for numerical computation
# fast operation on large data set 
# mathematical , logical and statistical opeartions
# integration with other python librabies , pandas ,scikit-learn 


from numpy import *
arr = array([1,2,3,4,5,6])
print(arr)
print("type:",type(arr))
print("data type:",arr.dtype)

# program 2
arr2 = array([1.5,2.5,3.6,4.7,5.8,6.9])
print(arr2)
print("type:",type(arr2))
print("data type:",arr2.dtype)
print(arr2.ndim)


# 2D array
martixA = array([[11,22,33],[44,55,66]])
print(martixA) # matrix
print(martixA.ndim) # dimension
print(martixA.shape) # rows and columns


# string array
print(array(["chinmay","sarika","poorva"]))

# float integer combine
arrayB = array([11,22,33,23.4])
print(arrayB.dtype)


# program 2
martixA = array([[11,22,33],[44,55,66]])
print(martixA) # matrix
print(martixA.ndim) # dimension
print(martixA.shape) # rows and columns

print(martixA.ndim)
print(martixA.shape)
print(martixA.dtype)
print(martixA.size)
print(martixA.itemsize)


# program3 

matrixC = array([11,22,33])
print(matrixC+1)
print(matrixC*2)
print(matrixC/4)
print(matrixC%4)

