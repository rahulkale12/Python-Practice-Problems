#3.Write a Function to Find the Greatest Common Divisor (GCD) of Two Numbers:


def GCD(a,b):
    while b:
        a,b = b, a%b
    return a

a= 56
b = 98
print(GCD(a,b))



#second way

def GCD(a,b):
    smallest = min(a,b)
    gcd_value = 1

    for i in range(1, smallest+1):
        if a%i == 0 and b %i ==0:
            gcd_value = i

    return gcd_value
    
a = 56
b = 98
print(GCD(a,b))