#2.Count the Occurrences of an Element in a Tuple:

a = (1,2,3,4,5,5,6,7,7,8,8,8,9,10)
occurence= {}
element = 8
for ele in a:
    if ele not in occurence:
        occurence[ele]=1
    else:
        occurence[ele]+=1

max_element = max(occurence,key= occurence.get)
print(max_element,occurence[max_element])
print(occurence)



#2nd way
# a = (1,2,3,4,5,5,6,7,7,8,8,8,9,10)
# element = 8
# print(a.count(element),element)  

