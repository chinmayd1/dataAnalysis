import pandas as pd
# write to CSV

df = pd.DataFrame({
    "ID":[101,102,103],
    "Name":["akash","amol","ajay"],
    "Salary":[50000,60000,70000]
})
print(df)
# program 1 writing with index
#df.to_csv('emplyee_output.csv')

# program 2
# writing without index
df.to_csv('emplyee_output.csv',index=False)

# program 3
# writing CSV usually with |
df.to_csv('employee2_output.csv',index=False,sep='|')

# program 4
# witing to excel
# pip install openpyxl

#df.to_excel('employees3.xlsx',index= False)

# writing to excel file using sheet name
#df.to_excel('employees4.xlsx',index= False,sheet_name='EmployeeData')

# writing dataframe to json

df.to_json('employee.json')

# to make more readle
df.to_json('employee2.json',orient='records')


