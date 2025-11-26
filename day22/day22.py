import pandas as pd
data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan"],
    "Age": [25, 30, 35, 28, 40],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 60000, 70000, 55000, 65000]
}

df = pd.DataFrame(data)
print(df)

# select a salary greater than 55
print(df[["Salary"]])
print(df[df["Salary"] > 55000])

ee = (df["Salary"] > 55000)
print(ee)
print(df[ee])

print(df)

# print employee of ID
ee2 = (df["Department"] == "IT")
print(ee2)
print(df[ee2])

# print employee of IT and salary greater than 55
print("------------------------------")
ee3 = (df["Department"] == "IT") & (df["Salary"] > 55000)
print(ee3)
print(df[ee3])

# print user of department IT or HR
print(df)
ee4 = (df['Department'] == "IT") | (df['Department'] == "HR")
print(ee4)
print(df[ee4])

# Sorting of data 
sortedVaue = df.sort_values(by="Salary",ascending=False)
print(sortedVaue)
sortedVaue = df.sort_values(by="Salary")
print(sortedVaue)
