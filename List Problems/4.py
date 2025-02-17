#4.Find the Second Largest and Second Smallest Numbers in a List:

a = [1,2,3,4,6,7,5,6,8]
unique = set(a)
sorting = list(sorted(unique))
print(sorting[1]) #2 second smallest
print(sorting[-2]) #7 second largest



# using function

# def smallest_largest(arr):
#     unique = list(set(arr))
#     unique.sort()
#     return unique[1],unique[-2]

# smallest, largest = smallest_largest([1,1,2,3,4,5,6,8,7])
# print("second smallest is :",smallest)
# print("second largest is :",largest)
