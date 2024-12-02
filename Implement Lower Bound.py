#Python code
def lowerBound(arr: [int], n: int, x: int) -> int:
    low,high=0,n
    while low<high:
        mid=(low+high)//2
        if arr[mid]<x:
            low=mid+1
        else:
            high=mid
    return low
