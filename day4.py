
import mypack.arith1 
e = mypack.arith1.addition(13,4)
print(e)


import mypack.arith1 as ar
e2 = ar.addition(23,4)
print(e2)

from mypack.arith1  import addition
from mypack.arith2 import subtraction

e3 = addition(10,4)
e4 = subtraction(6,3)
print(e3)
print(e4)

from mypack.arith1 import *
from mypack.arith2 import *

e5 = addition(23,4)
e6 = subtraction(23,4)
print(e5)
print(e6)