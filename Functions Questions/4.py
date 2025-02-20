#4.Write a Function to Find the Lowest Common Multiple (LCM) of Two Numbers:


def LCM(a,b):
    greatest= max(a,b)
    while True:
        if greatest%a == 0 and greatest %b == 0:
            return greatest
        greatest+=1

print(LCM(12,18))



#second way using for loop to calculate lcm using for loop we need to take gcd as well.

def GCD(a,b):
    while b:
        a, b = b , a%b

    return a

def LCM(a,b):
    return (a*b) // GCD(a,b)

a= 12
b = 18
print(LCM(a,b))