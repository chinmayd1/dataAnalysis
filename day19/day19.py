# +----+---------+-------+----------+
# | ID | Name    | Age   | Salary   |
# +----+---------+-------+----------+
# | 1  | Alice   | 25    | 50000    |
# | 2  | Bob     | 30    | 60000    |
# | 3  | Charlie | 35    | 70000    |
# +----+---------+-------+----------+

# What is a data frame ??
# A 2D table (rows + columns)
# Like Excel or SQL 
# Each column has different data types
# Build on numpy 

# A data frame from python  dictionary

import pandas as pd

data = {
    "Name":["Chinmay","Sarika","Poorva"],
    "Age":[25,30,40],
    "Salary":[50000,60000,70000]
}
df = pd.DataFrame(data)
print(df)

data2 = [
    {"Name":"Alice","Age":25,"Salary":50000},
    {"Name":"Bob","Age":30,"Salary":500000},
    {"Name":"Shawn","Age":35,"Salary":50000000}
]
df2 = pd.DataFrame(data2)
print(df2)

import numpy as np
arr = np.array([
    [1,'sarika',25],
    [2,'bob',30],
    [3,'charlie',35]
])

df3 = pd.DataFrame(data=arr,columns=["ID","Name","Age"])
print(df3)


df4 = pd.read_csv('employees.csv')
print(df4)

print('first 5 -----------------')
firstFive = df4.head()
print(firstFive)
print('last 5-------------------')
lastFive = df4.tail()
print(lastFive)

# colum data types
print(df4.dtypes)
print(df4.describe())


print(df4.shape)
print(df4.columns)
print(df4[['Name','Department']])


a = df4['Salary'] > 55000
print(df4[a])