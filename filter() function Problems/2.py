#2.Write a Program Using filter() to Find All Strings in a List That Start with the Letter 'A': ["apple", "banana", "avocado", "grape"]:

words = ["apple", "banana", "avocado", "grape"]
z = list(filter(lambda x: x[0].lower()=="a",words))
print(z)    



#second way using startswith method.

words = ["apple", "banana", "avocado", "grape"]
z = list(filter(lambda x: x.startswith('a'),words))
print(z)    