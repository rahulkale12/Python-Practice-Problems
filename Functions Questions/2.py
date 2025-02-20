#2.Write a Function to Check a number is Prime or Not:

def Prime(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

print(Prime(7))



# To generate prime numbers in given range.

def Prime(n):
    primes = []

    for num in range(2, n+1):
        is_Prime = True

        for i in range(2, num):
            if num%i ==0:
                is_Prime= False
                break
        if is_Prime:
            primes.append(num)

    return primes

n = 10
print(Prime(n))
