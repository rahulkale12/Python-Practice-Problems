#9.Use map() to Convert a List of Binary Strings into Integers: ["101", "111", "1001"]:

a = ["101", "111", "1001"]

z = list(map(lambda x: int(x,2), a))
print(z)