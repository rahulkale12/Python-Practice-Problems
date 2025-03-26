#1. Counting unique vowels in a string.


vowels= ["a","e","i","o","u"]
count = 0
taken = ""
word = "Rahul  Kale"
for i in word:
    if i in vowels and i not in taken:
        taken+=i
        count+=1
print(count)



# second way
vowels= ["a","e","i","o","u"]
taken = ""
word = "Rahul  Kale"
for i in word:
    if i in vowels and i not in taken:
        taken+=i
print(len(taken))



#third way using set for unique.

vowels= ["a","e","i","o","u"]
taken = set()
word = "Rahul  Kale"
for i in word:
    if i in vowels and i not in taken:
        taken.add(i)
print(len(taken))
