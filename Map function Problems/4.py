#5.Write a Program Using map() to Compute the Length of Each Word in a List: ["apple", "banana", "cherry"]:

l=["apple", "banana", "cherry"]
z = list(map(lambda x: len(x),l))
print(z)