#8. Print Prime numbers in a nth range.

def prime_range(a,b):

    primes = []
    
    for i in range(a,b+1):
        if i<2:
            continue
        is_prime = True
        for j in range(2,i):
            if i%j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes
        

a = 2
b = 10
print(prime_range(a,b))




#without using flag

def prime_range(a,b):

    primes = []
    
    for i in range(a,b+1):
        if i>1:
            for j in range(2,i):
               if i%j == 0:
                 break
            else:
                 primes.append(i)
    return primes
        

a = 2
b = 10
print(prime_range(a,b))