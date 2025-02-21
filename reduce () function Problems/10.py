#10.Write a Program Using reduce() to Combine a List of Tuples by Summing Their Corresponding Elements: [(1, 2), (3, 4), (5, 6)]:


from functools import reduce

l = [(1, 2), (3, 4), (5, 6)]

z = reduce(lambda x,y : (x[0]+y[0],x[1]+y[1]),l)   
print(z)
