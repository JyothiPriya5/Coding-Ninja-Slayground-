#Python code
from os import *
from sys import *
from collections import *
from math import *
def addOneToNumber(arr):
    n = len(arr)
    carry = 1 
    for i in range(n - 1, -1, -1):
        sum_ = arr[i] + carry
        arr[i] = sum_ % 10
        carry = sum_ // 10
    if carry:
        arr.insert(0, carry)
    while len(arr) > 1 and arr[0] == 0:
        arr.pop(0)
    return arr
def main():
    results = []
    for _ in range(T):
        N = int(input())  
        Arr = list(map(int, input().split()))
        results.append(addOneToNumber(Arr))
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
