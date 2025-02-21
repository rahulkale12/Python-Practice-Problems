#5.Flatten a 2D List into a 1D List:
my_list = [[1, 2], [3, 4], [5, 6]]
z = [final for sub in my_list for final in sub]
print(z)