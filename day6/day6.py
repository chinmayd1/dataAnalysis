import array
arrOne  = array.array('i',[11,22,33,44,5,55,66,77,55])
arrTwo = array.array('i',[111,222,333])

# append()
arrOne.append(11)
print(arrOne)

# count
print(arrOne.count(55))

#extend()
arrOne.extend(arrTwo)
print(arrOne)

# fromFile()
import array as arr
# open file object for writing
f = open('my_file.txt','wb') # 
#write array of integers to file object
arr1=arr.array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Array in the file :",arr1 )
arr1.tofile(f)
#close file
f.close()

# #open file for reading
f = open('my_file.txt','rb') # read
#initialize array with integer type
array_one = arr.array("i")  # arr one define with type
#initialize array with integer type
array_two = arr.array("i") # arr two define with type
#read 3 items from file
array_one.fromfile(f,3) # add elements from file to array_one 
print("Appended array1 :",array_one)
#Moving the cursor to the first position
f.seek(0) #   return to zero
#read 6 items from file
array_two.fromfile(f,6) # add the elements to array_two
print("Appended array2 :",array_two)
#close file
f.close()

# fromlist
lst = [11,22,33,44,55]
array_three = arr.array("i")
array_three.fromlist(lst)
print(array_three)


# fromstring 
#str2 = "chinmay"
#array_four = arr.array('s')
#array_four.fromstring(str2)

arrOne  = array.array('i',[11,22,33,44,5,55,66,77,55])
print(arrOne.index(22))
arrOne.insert(1,333)
print(arrOne)

arrOne.pop()
arrOne.pop(1)
arrOne.remove(11)
arrOne.reverse()
print(arrOne.tolist())


print(arrOne.itemsize)
print(arrOne.typecode)


# linear search 
# index search 
# bubble sort 
# single dimensional # numpy
# multiple dimentional # numpy

