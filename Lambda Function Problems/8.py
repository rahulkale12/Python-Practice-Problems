#8.Use a Lambda Function with reduce() to Find the Product of All Elements in a List:

from functools import reduce
numbers = [1, 2, 3, 4]
z = reduce(lambda x,y: x*y, numbers)
print(z)