//Python Code
from math import *
from collections import *
from sys import *
from os import *

## Read input as specified in the question.
## Print output as specified in the question.
def Fibonacci(n):
    if n==1 or n==2:
        return 1
    f1,f2=1,1
    for _ in range(3,n+1):
        f3=f1+f2
        f1,f2=f2,f3
    return f3  
n=int(input())
print(Fibonacci(n))
