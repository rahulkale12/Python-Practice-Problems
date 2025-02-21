#8.Write a Program Using filter() to Find All Palindrome Strings in a List: ["level", "python", "radar", "java"]:


l = ["level", "python", "radar", "java"]
z = list(filter(lambda x : x[::-1]==x, l))
print(z)