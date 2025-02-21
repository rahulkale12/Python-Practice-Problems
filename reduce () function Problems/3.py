#3. Use reduce() to Find the Largest Number in a List: [10, 20, 5, 40, 30]:

from functools import reduce
l = [10, 20, 5, 40, 30]
z = reduce(lambda x,y: x if x>y else y,l)
print(z)
