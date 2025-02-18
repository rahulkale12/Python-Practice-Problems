#Create a Set and Perform Union, Intersection, and Difference Operations with Another Set:

set1= {1,2,3}
set2= {3,4,5}

# union #################################
union = set1 | set2
print(union)
set3 = set1.union(set2)
print(set3)

#### intersection ######################
intersection = set1 & set2
print(intersection)

set4 = set1.intersection(set2)
print(set4)

# Difference ##########################

difference = set1 -set2
print(difference)

set5= set1.difference(set2)
print(set5)