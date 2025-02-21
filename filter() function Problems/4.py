#4.Write a Program Using filter() to Filter Out All Non-Vowel Characters from a String "hello world":

l="hello world"
vowels = "aeiouAEIOU"
z  = ''.join(filter(lambda x: x in vowels,l))
print(z)