#14.Create a function to check if a number is Perfect or Not:

def Check_Perfect(n):
    sum = 0
    if n<2:
        return False
    for i in range(1,n):
        if n%i == 0:
            sum +=i
    
    return sum == n

n = 8
print(Check_Perfect(n))