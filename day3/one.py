# os
# program 1
import os 
print(os.getcwd())
# C:\Users\chinm\Desktop\DataAnalysis

# program 2
#list all files and folder in working directory
print(os.listdir())
print(os.listdir("C:/Users/chinm/Desktop/DataAnalysis/mypack"))

#program 3
print(os.getcwd())
# make a new directory 
#os.mkdir("mypack2") # create a folder
#os.makedirs("mypack3/pack2/pack1")# create a nested folder

#program  4
#remove the directory
#os.rmdir("mypack2")
#os.removedirs("mypack3/pack2/pack1")

# check if a path is a file or  folder
#os.mkdir("mypackfive")
e = os.path.isdir('mypackfive')
print(e)
e2 = os.path.isfile('cities.bin')
print(e2)

print(os.getcwd())

os.chdir('C:/Users/chinm/Desktop/DataAnalysis/mypack')
print(os.getcwd())
