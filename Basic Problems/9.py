#9. Find fibonacci of nth number.

def fib(n):
    if n ==0:
        return 0
    if n == 1:
        return 1
    a,b = 0,1

    for i in range(2,n+1):
        a,b = b, a+b

    return b

print(fib(3))



# using recursion
def fib(n):
    if n==0:
        return 0
    if n ==1:
        return 1
    
    return fib(n-1) + fib(n-2)
print(fib(3))