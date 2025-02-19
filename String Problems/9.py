#9.Count the Occurrences of Each Word in a Given String:

word = "Hello World Hello World Python"
seen = {}
for i in word.split():
    if i not in seen:
        seen[i]=1
    else:
        seen[i]+=1
print(seen)

