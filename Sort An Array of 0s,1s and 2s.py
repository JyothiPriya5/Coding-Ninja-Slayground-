#Python code
from os import *
from sys import *
from collections import *
from math import *

def sortArray(arr, n):
	arr.sort()
	return arr
if __name__=="_main_":
	n=int(input())	
	for i in range(n):
		arr=list(map(int,input().split()))
	x=sortArray(arr,n)
	print(x)					
