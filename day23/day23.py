import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
    "Age": [25, 30, 35, 28, 40],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 60000, 70000, 55000, 65000]
}

df = pd.DataFrame(data)
print(df)

# filter salary > 60000
e1 = df["Salary"] > 60000
print(e1)
salaryAbove60 = df[e1]
print(salaryAbove60)

# program 2
# print only IT department empployees
print(df)
e2 = df["Department"] == "IT"
print(e2)
print(df[e2])

#filter using two conditions 
# IT | HR
e3 = (df["Department"] == "IT") | (df["Department"] == "HR")
print(e3)
print(df[e3])

#filter using two conditions 
# IT and salary > 60000
e4 = (df["Department"] == "IT") & (df["Salary"] >= 60000)
print(e4)
print(df[e4])

# filtering operation based on sorting
print(df)
e1 = df.sort_values(by="Salary",ascending=False)
print(e1)

e2 = df.sort_values(by="Salary")
print(e2)

# Add a conditional columns if salary > 60000 ---> HIGH or LOW
df["Level"] = df["Salary"].apply(lambda x:"High" if x > 60000 else "Low")
print(df)

# salary above 55000 and below 65000
mid_salary = (df["Salary"] >= 55000) & (df["Salary"] <= 65000)
print(mid_salary)
print(df[mid_salary])

# select the records not belong to IT or HR department

e3 = ~(df["Department"].isin(["HR","IT"]))
print(e3)
print(df[e3])