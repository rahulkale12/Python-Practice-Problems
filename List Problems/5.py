#5.Remove All Duplicate Elements While Maintaining the Order:

a = [1,2,3,4,5,5,6,6,7,9,8]
result = []
seen = set()

for ele in a:
    if ele not in seen:
        result.append(ele)
        seen.add(ele)
print(result)
        

#using function

# def remove_duplicate(arr):
#     result = []
#     seen = set()
#     for ele in arr:
#         if ele not in seen:
#             result.append(ele)
#             seen.add(ele)
#     return result

# print(remove_duplicate([1,2,3,3,5,5,4]))