#10.Write a Program Using map() to Reverse Each String in a List: ["python", "map", "example"]:

strings = ["python", "map", "example"]
z = list(map(lambda x: x[::-1],strings))
print(z)