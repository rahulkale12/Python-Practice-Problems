#8.Write a Dictionary Comprehension to Filter Out All Key-Value Pairs in a Dictionary Where the Key Is a Vowel:

my_dict = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5, 'b': 6, 'c': 7}

z = {x:y for x,y in my_dict.items() if x in "aeiouAEIOU"}
print(z)