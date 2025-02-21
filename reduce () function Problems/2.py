#2.Write a Program Using reduce() to Find the Product of All Elements in a List: [2, 3, 4]:

from functools import reduce

l = [2,3,4]
z = reduce(lambda x,y: x*y,l)
print(z)