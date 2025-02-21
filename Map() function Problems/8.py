#8.Write a Program Using map() to Multiply Corresponding Elements of Two Lists: [1, 2, 3] and [4, 5, 6]:

a = [1,2,3]
b = [4,5,6]
z = list(map(lambda x,y: x*y , a,b))
print(z)