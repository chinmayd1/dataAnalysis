# difference between array and list 
import array
#                    0  1  2   3  4  5  6
x = array.array('i',[10,11,12,13,14,15,16])
#                   -7  -6 -5 -4 -3 -2 -1

print(x[-4:-1])
print(x[0:7:2])


# program 1
# print(x)
# print(type(x))

# # indexing and slicing 
# #x[start:stop:stride]
# a = x[1:4]
# print(a)

# b = x[0:]
# print(b)

# c =x[:4]
# print(c)


# program 3
import array
#                      0  1  2  3  4 5  6  7
h11 = array.array('i',[11,22,33,44,5,55,66,77])
h1 = h11[1:4]
print(h1)
for x in h11[1:4]:
    print(x)

for x in h11[6:]: #[66,77]
    print(x)


# program 4
h11 = array.array('i',[11,22,33,44,5,55,66,77,55])
h11.append(33)
print(h11)

e1 = h11.count(55)
print(e1)

h11.insert(2,222)
print(h11)

h11.remove(77)
h11.pop()
print(h11)
print(h11)