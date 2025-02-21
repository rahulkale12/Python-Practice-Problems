#5.Write a Lambda Function with map() to Convert a List of Strings to Uppercase:

strings = ["hello", "world"]
z = map(lambda x: x.upper(),strings)
print(list(z))