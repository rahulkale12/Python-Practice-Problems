#7.Use map() to Combine Two Lists Element-Wise into a List of Tuples: [1, 2, 3] and ["a", "b", "c"]:

a = [1,2,3,]
b = ["a","b","c"]
z = list(map(lambda x,y: (x,y),a,b))
print(z)