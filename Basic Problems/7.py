#7. Find the prime number of nth number.

def prime_num(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

        
print(prime_num(2))
print(prime_num(3))
print(prime_num(6))
print(prime_num(4))
print(prime_num(9))
