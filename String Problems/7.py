#7.Find the First Non-Repeating Character in a String:

word = "hello"
for i in word:
    if word.count(i)== 1:
        print(i)

         