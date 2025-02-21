#3.Use map() to Convert a List of Temperatures in Celsius [0, 20, 37, 100] to Fahrenheit:

l = [0,20,37,100]
z = list(map(lambda x: (x*9/5)+32,l))
print(z)
