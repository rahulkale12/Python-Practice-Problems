#7.Invert a Dictionary (Keys Become Values and Vice Versa):

my_dict = {'banana': 10, 'apple': 25, 'cherry': 15}

z = {key:value for value,key in my_dict.items()}
print(z)