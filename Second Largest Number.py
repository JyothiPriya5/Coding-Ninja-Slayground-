//Python code
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    if n==1:
        return a
    a.sort()
    ans=[]    
    if n==2:
        ans.append(a[0])
        ans.append(a[-1])

    ans.append(a[-2])
    ans.append(a[1])
    return ans

    
