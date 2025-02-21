#6.Generate a Dictionary from a List of Numbers Where the Key Is the Number and the Value Is "Even" or "Odd":

my_list = [1,2,3,4,5,6]
z = {x:("Even" if x%2==0 else "Odd")for x in my_list}
print(z)