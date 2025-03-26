#2. Counting consonants in a string.

vowels= ["a","e","i","o","u"]
count = 0
word = "Programming"
for i in word:
    if i not in vowels:
        count+=1
print(count)