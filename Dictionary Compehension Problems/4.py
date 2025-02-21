#4.Create a Dictionary That Maps Each Character in a String to Its Frequency:

my_str = "hello"
z ={x: my_str.count(x) for x in my_str}
print(z)