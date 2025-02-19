#8.Convert a String to Title Case Without Using title():

word = "hello world"
new = word.split()
final = " ".join(i.capitalize() for i in new)
print(final)