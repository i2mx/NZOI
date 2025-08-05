from functools import reduce
print(reduce(lambda x,y:26*x+y,map(lambda x:ord(x)-64,input()),0))
