#8.Write a Program Using reduce() to Count the Total Number of Characters in a List of Strings: ["python", "reduce", "example"]:

from functools import reduce

l= ["python", "reduce", "example"]

z = reduce(lambda x,y : x+len(y),l,0)  #setting 0 as initial value o x => 0+6 =6, 6+6 = 12, 12+ 7 = 19
print(z)