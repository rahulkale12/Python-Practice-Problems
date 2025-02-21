#4.Write a Program Using reduce() to Find the Smallest Number in a List: [15, 8, 22, 3, 9]:

from functools import reduce

l = [15, 8, 22, 3, 9]
z = reduce(lambda x,y: x if x<y else y,l)
print(z)