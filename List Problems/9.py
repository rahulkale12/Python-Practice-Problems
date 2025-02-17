#9.Create a List of Squares of Even Numbers from 1 to 20:

a = [x**2 for x in range(1, 21)if x%2==0]
print(a)