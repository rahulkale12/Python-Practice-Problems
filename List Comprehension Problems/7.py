#7.Filter Out All Vowels from a Given String:

my_str = "Animal"
vowels = "aeiouAEIOU"
z = [char for char in my_str if char not in vowels]
print(z)