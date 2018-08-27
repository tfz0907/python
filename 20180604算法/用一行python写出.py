#用一行python写出1+2+3+…+10**8 ；
from functools import reduce

a = reduce(lambda x, y: x+y, range(1, 10**8))
print(a)