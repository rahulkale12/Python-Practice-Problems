#6.Use a Lambda Function to Sort a List of Tuples by the Second Element:

tuples = [(1, 2), (3, 1), (5, 4)]

z = sorted(tuples, key = lambda x: x[1])
print(z)