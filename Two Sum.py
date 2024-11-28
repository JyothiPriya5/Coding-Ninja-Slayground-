//Two pointer Approach
//Python Code
def read(n: int, book: [int], target: int) -> str:
    for i in range(n):
        for j in range(i+1,n):
            if book[i]+book[j]==target:
                return "YES"
    return "NO"            
