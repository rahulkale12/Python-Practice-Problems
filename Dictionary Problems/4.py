#4.Sort a Dictionary by Its Keys and Values:

my_dict = {'banana': 10, 'apple': 25, 'cherry': 15}

#sorting by keys

sorted_keys = dict(sorted(my_dict.items()))
print(sorted_keys)


#sorting by values

sorted_values = dict(sorted(my_dict.items(), key = lambda x: x[1]))   #as items return a list of tuple where there is key and value so, here sorting out with values

print(sorted_values)