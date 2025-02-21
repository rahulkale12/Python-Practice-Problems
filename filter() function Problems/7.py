#7.Use filter() to Keep Only Positive Numbers from a List: [-10, 20, -30, 40, 0, 50]:

l = [-10, 20, -30, 40, 0, 50]
z = list(filter(lambda x: x>0 , l))
print(z)