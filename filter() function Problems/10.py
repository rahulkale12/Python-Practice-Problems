#10.Write a Program Using filter() to Find All Numbers in a List That Are Divisible by 3: [3, 5, 9, 12, 14, 18]:


l = [3, 5, 9, 12, 14, 18]
z = list(filter(lambda x : x%3==0,l))
print(z)