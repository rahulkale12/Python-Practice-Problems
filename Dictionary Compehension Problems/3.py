#3.Write a Dictionary Comprehension to Filter a Dictionary, Keeping Only the Items Where the Value Is Greater Than 10:
my_dict = {"apple":10,"banana":20,"grapes":15,"chiku":18,"mango":8,"pineapple":5}
z = {x:y for x,y in my_dict.items() if y>10}
print(z)