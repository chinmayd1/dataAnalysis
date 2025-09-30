
#chinmay sarika amol
# 7 , 6  , 4
#chinmay             " 20 bytes
#sarika              " 20 bytes
#amol                " 20 bytes


#program 1
# reclen = 20
# with open('cities.bin','wb') as f:
#     n = int(input('how many names you want to enter:')) # 5
#     for x in range(n):
#         city = input("enter the cityname ") #"nagpur"
#         city = city + (20 - len(city)) * " " # "pune                    "
#         city = city.encode()
#         f.write(city)

# reclen = 20
# with open('cities.bin' , 'rb') as f:
#     n = int(input('which record you want to read ?')) #3
#     f.seek(reclen*(n-1))
#     str = f.read(reclen)
#     str = str.decode()
#     print(str)



# total number of cities ---> total file size ---> 20 --- total cities 
# import os
# reclen = 20 
# size = os.path.getsize('cities.bin') # 60
# n = int(size/ reclen)  # 3

# with open('cities.bin','rb') as f:
#     name  = input('enter the city') # pune
#     name  =  name + (20 - len(name)) * " " 
#     name = name.encode()

#     position = 0
#     found = False

#     for  i in range(n):
#         f.seek(position)
#         str = f.read(20)
#         if str == name:
#             found = True
#             print('city found in file')
#         position = position + reclen

# if not found:
#     print('city not found')




# find the string and update 
# 80

# import os 
# reclen = 20
# size = os.path.getsize('cities.bin')
# n = int(size/reclen)
# print(n)

# with open("cities.bin",'r+b') as f:
#     name = input('enter the city name') #'pune'
#     name = name + (reclen - len(name)) * " "
#     name = name.encode()

#     newname = input('enter the updated name ')
#     newname = newname + (reclen - len(newname)) * " "
#     newname = newname.encode()

#     position = 0
#     found = False
#     for i in range(n):
#         f.seek(position)
#         str = f.read(reclen)
#         print(str)
#         if str == name:
#             found = True
#             f.seek(-20,1)
#             f.write(newname)

#         position = position + reclen
    
#     if not found:
#         print("city not found")

    
# find the string and delete
#  file names ---> only those name which we want and then rename file

import os

reclen  = 20
n = size = os.path.getsize('cities.bin')
f1 = open('cities.bin','rb')
f2 = open('cities2.bin','wb')
cityname = input('Enter the city , which you want to delete ...') #nagpur
cityname = cityname + (reclen - len(cityname))*" "
cityname = cityname.encode()
for i in range(n):
    str = f1.read(20)
    if str != cityname:
        f2.write(str)
f1.close()
f2.close()
os.remove('cities.bin')
os.rename('cities2.bin','cities.bin')












