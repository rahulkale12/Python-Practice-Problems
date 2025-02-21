#1.Use filter() to Extract All Even Numbers from a List of Integers [1, 2, 3, 4, 5, 6]:

l=[1, 2, 3, 4, 5, 6]
z = list(filter(lambda x:x%2==0,l))
print(z)

