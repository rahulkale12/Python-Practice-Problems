#5.Write a Dictionary Comprehension to Swap Keys and Values of a Dictionary:

my_dict = {"apple":10,"banana":20,"grapes":15,"chiku":18,"mango":8,"pineapple":5}

z = {x:y for y,x in my_dict.items()}
print(z)
