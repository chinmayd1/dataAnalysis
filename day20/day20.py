# Day 2 — Reading & Writing Data (CSV, Excel, JSON)
# Today’s Learning Goals
# Read CSV files
# Read Excel files
# Read JSON files
# Save (write) DataFrames to files
# Important parameters (sep, header, names, index_col)
# Handling missing data while reading


# reading csv file
import pandas as pd
df = pd.read_csv("students.csv")
print(df)

# reading csv without header
# df = pd.read_csv("data.csv",header =None)
# print(df)

# add your own column names
df = pd.read_csv("data.csv",header=None,names=['name', 'age', 'city'])
print(df)

print('------------------------')
# Example 3 :  Specific column as index
df = pd.read_csv("students.csv",index_col ="name")
print(df)

df = pd.read_csv("marks.txt",sep="|")
print(df)

# program 4
# reading a excel file 
# pip install openpyxl
# pip install numpy
# pip install pandas

df = pd.read_excel('employees.xlsx')
print(df)

# program 5
# reading the the specific excel sheet
# df = pd.read_excel('employees.xlsx',sheet_name = "sheet1")
# print(df)
print('--------------------------------------------------')
df = pd.read_excel('employees.xlsx',header = None)
print(df)

# program 6
# reading json file 
df = pd.read_json('data.json')
print(df)

# program 7
# limiting the count of rows
df = pd.read_csv("students.csv",nrows=1)
print(df)

# writing back to json , csv and excel
