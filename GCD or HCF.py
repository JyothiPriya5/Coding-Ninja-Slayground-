//Python code
def calcGDC(n: int, m: int) -> int:
    while m != 0:
        temp = m
        m = n % m
        n = temp
    return n
