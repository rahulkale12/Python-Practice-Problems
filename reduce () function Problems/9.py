#9. Use reduce() to Generate the Cumulative Sum of a List of Numbers: [1, 2, 3, 4, 5]:

from functools import reduce

l = [1, 2, 3, 4, 5]
z = reduce(lambda x,y : x+[x[-1]+y] if x else [y],l,[])
print(z)

