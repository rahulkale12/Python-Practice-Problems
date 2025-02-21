#6.Write a Program Using map() to Replace Every Vowel in a List of Strings with '*': ["hello", "world", "python"]:


my_str =["hello", "world", "python"]
z = list(map(lambda x: " ".join('*' if chr in 'aeiouAEIOU' else  chr for chr in x),my_str))
print(z)