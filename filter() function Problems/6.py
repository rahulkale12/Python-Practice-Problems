#6.Write a Program Using filter() to Extract All Words in a List That Have More Than 5 Characters: ["python", "map", "filter", "reduce"]:

l =["python", "map", "filter", "reduce","java","C++"]
z = list(filter(lambda x: len(x)>5,l))
print(z)