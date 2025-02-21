#2.Convert a List of Words into a Dictionary Where the Keys Are the Words and the Values Are Their Lengths:

my_list = ["python","java","ruby","c++"]
z = {x:len(x) for x in my_list}
print(z)