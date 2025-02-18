#4.Add and Remove Elements from a Set Dynamically Using Input from the User:
set1 = {1,2,3,4}
print(set1)
user_add = int(input("enter a number to add:"))
set1.add(user_add)
print(set1)

user_remove = int(input("enter a number to remove:"))
set1.discard(user_remove)
print(set1)
