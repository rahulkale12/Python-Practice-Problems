#2.Write a Program Using map() to Capitalize All the Strings in a List: ["python", "django", "aws"]:

strings = ["python", "django", "aws"]
z = list(map(lambda x: x.capitalize(),strings))
print(z)