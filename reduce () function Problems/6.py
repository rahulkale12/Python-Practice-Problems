#6.Write a Program Using reduce() to Calculate the Factorial of a Number Using a List: [1, 2, 3, 4, 5] for 5!:

from functools import reduce

l = [1, 2, 3, 4, 5] 
z = reduce(lambda x,y: x*y,l)
print(z)