#5.Use filter() to Find All Prime Numbers in a List of Integers [2, 3, 4, 5, 6, 7, 8, 9, 10]:

def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
z = list(filter(prime,arr))
print(z)


#optimized approach

def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5+1)):
        if n%i ==0:
            return False
    return True
arr = [2, 3, 4, 5, 6, 7, 8, 9, 10]
z = list(filter(prime,arr))
print(z)