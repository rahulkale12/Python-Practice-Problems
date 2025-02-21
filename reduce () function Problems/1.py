#1.se reduce() to Find the Sum of All Numbers in a List: [1, 2, 3, 4, 5]:

from functools import reduce

l= [1, 2, 3, 4, 5]
z = (reduce(lambda x,y: x+y,l))
print(z)