
# What is pandas ?
# How  to install / import pandas
# Series and Data frames basics
# Creating a series 
# Creating a data frame 
# Accessing data

import pandas as pd
# import pandas
# from pandas import Series
# from pandas import *

# program 2
s = pd.Series([10,20,30,40])
print(s)
s2 = pd.Series([100,200,300],index=['a','b','c'])
print(s2)

# program 3
marks = {"math":88,"science":92,'english':85}
print(marks)
s3 = pd.Series(marks)
print(s3)

# A data frame is 2D table 
# dictionary of list
data = {
    'name':['chinmay','sarika','Mike'],
    'age':[25,30,22],
    'city':["Delhi","Mumbai","Pune"]
}
df = pd.DataFrame(data)
print(df)

# Data frame using dictionary 

data2 = [
    {"name":"Akshaya","salary":2000},
    {"name":"Riya","salary":3000},
    {"name":"Karan","salary":5000}
]
data2 = pd.DataFrame(data2)
print(data2)

# Accessing the columns
print(data2['salary'])
# Accessing the multiple columns
print(data2[['salary','name']])
# Accesing rows using .loc(indexlabe) and iloc(row number)

print(data2.loc[1])
print(data2.iloc[0])

# label 0 , 1, 2
# 0    2000  Akshaya     #0
# 1    3000     Riya     #1
# 2    5000    Karan     #2

# A    2000  Akshaya     #0
# B    3000     Riya     #1
# C    5000    Karan     #2

print(data2.info())
print(data2.describe())