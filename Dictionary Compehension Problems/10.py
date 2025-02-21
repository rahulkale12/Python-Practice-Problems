#10.Convert Two Lists into a Dictionary Using Comprehension:

keys = ["name", "age", "city"]
values = ["Alice", 25, "New York"]

z = {keys[i]:values[i] for i in range(len(keys)) }
print(z)