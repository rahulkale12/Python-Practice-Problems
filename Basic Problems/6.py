#6. Find the factorial of a nth number.

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

print(factorial(5))



#using recursion

def factorial(n):
    if n==1: 
        return 1
    elif n == 0:
        return 0
    
    return n * factorial(n-1)

print(factorial(5))