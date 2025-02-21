#5.Use reduce() to Concatenate a List of Strings into a Single String: ["hello", "world", "python"]:


from functools import reduce

l=["hello", "world", "python"]

z = reduce(lambda x,y:x+ " " +y,l)
print(z)