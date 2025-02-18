#6.Remove a Key-Value Pair from a Dictionary Using a Specific Key:

my_dict = {'banana': 10, 'apple': 25, 'cherry': 15}

key = "banana"
if key in my_dict:
    del my_dict[key]

print(my_dict)
