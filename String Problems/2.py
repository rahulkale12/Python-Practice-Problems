#2.Count the Number of Vowels and Consonants in a String:

word = "rahul"
vowels = "aeiouAEIOU"
count_vowels = 0
consonants = 0
for i in word:
    if i in vowels:
        count_vowels+=1
    else:
        if i not in vowels and i.isalpha():
            consonants+=1
print(count_vowels)
print(consonants)



#second way using function

# def count_vowels_conso(word):
#     vowels = "aeiouAEIOU"
#     count_vowels= sum(1 for char in word if char in vowels)
#     count_consonants = sum(1 for char in word if char.isalpha() and char not in vowels)
#     return count_vowels,count_consonants

# print(count_vowels_conso("Rahul"))