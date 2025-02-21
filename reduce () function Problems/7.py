#7.Use reduce() to Calculate the GCD (Greatest Common Divisor) of a List of Numbers: [48, 60, 72]:

from functools import reduce
import math

l = [48,60,72]
z = reduce(math.gcd, l)
print(z)



#without math module

def GCD(a,b):
    while b:
        a,b = b, a%b
    return a

l = [48,60,72]
z = reduce(GCD, l)
print(z)