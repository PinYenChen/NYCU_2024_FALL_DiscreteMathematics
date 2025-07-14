#homework 1-1
def possibilities(n,k): # n共有幾點，k選幾點
    if k>n:
        return 0
    num = 1
    for i in range(n-k+1,n+1):
        num *= i
    denom = 1
    for i in range(1,k+1):
        denom *= i 
    return num//denom

def calculate(n):

    total = 1+possibilities(n,2)+possibilities(n,4)
    return total


x = int(input()) #x is the num of test
for j in range(1,x+1):
# 輸入點的數量
    n = int(input())
    print(calculate(n))
