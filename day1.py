# f = open('myfile.txt','w')
# str = input('please enter the name :')
# f.write(str)
# f.close()

# a python program to count the total number of words
# lines and characters

# "manasi is learning python".split()
# #["manasi","is","learning","python"]
# # len("manasi","is","learning","python"])


# import os , sys

# fname = input("Enter the fileName: ") # myfile.text
# if(os.path.isfile(fname)):
#     f = open(fname,'r')
# else:
#     print(f'File does not exist with name {fname}')

# cc = 0
# cl = 0
# cw = 0

# for line in f:
#     print(line)
#     words = line.split() #
#     cl = cl + 1
#     cw = cw + len(words)
#     cc = cc + len(line)
# print(cl)
# print(cw)
# print(cc)
# f.close()

# program 1
f1 =  open('viratkolhi.jpg','rb')
f2 =  open('new.jpg','wb')
bytes = f1.read()
f2.write(bytes)
f1.close()
f2.close()
# program 2
# file 
with open('sample.txt','w') as f:
    f.write('I am learning python \n')
    
with open('sample.txt','r') as f:
    print(f.read())

# txt , img 
# data

class Emp:
    # constructor
    def __init__(self,id,name,sal):
        self.name  =name
        self.sal = sal
        self.id = id

    def display(self):
        print(self.id)
        print(self.name)
        print(self.sal)


import pickle
f = open('emp.dat','wb')
noE = int(input("how many employees"))
for i  in range(noE):
    id  = input('Enter the id ')
    name = input('Enter the name')
    salary = input('Enter the salary')
    e = Emp(id,name,salary)
    pickle.dump(e,f)

f.close()



