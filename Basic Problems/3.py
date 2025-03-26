#3. Counting the number of occurence of a character in a string.

word = "Hello World"
count_char = {}
for i in word:
    if i != " ":
        if i not in count_char:
         count_char[i]=1
        else:
            count_char[i]+=1
print(count_char)



# second way using get() method
word = "Hello World"
count_char = {}
for i in word:
    if i != " ":
       count_char[i] = count_char.get(i,0)+1
        
print(count_char)
