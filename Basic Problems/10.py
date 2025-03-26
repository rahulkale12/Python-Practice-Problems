#10. Find fibonacci series in given nth range.

def fib(n):
    a,b = 0,1
    for i in range(n):
        print(a, end = " ")
        a,b = b, a+b
n = 10
fib(n)   



#using recursion
def fib(n):
    if n ==0:
        return 0
    if n ==1:
        return 1
    
    return fib(n-2) + fib(n-1)

n = 10
for i in range(n):
    print(fib(i),end= " ")


##############################################################

# start range and end range

def fib_range(start, end):
    a, b = 0, 1
    while a <= end:
        if a >= start:
            print(a, end=" ")
        a, b = b, a + b  

fib_range(10, 100)  


#using recusrsion

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def fib_range(start, end, n=0):
    value = fib(n)
    if value > end:  
        return
    if value >= start:  
        print(value, end=" ")
    fib_range(start, end, n + 1)  

fib_range(10, 100)