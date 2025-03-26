#5. Find the minimum number in a list.

def min_num(arr):
    min = arr[0]
    for i in range(len(arr)):
       if i<min:
           min = arr[i]
    return min

print(min_num([1,2,3,4]))



#second way using min()
def min_num(arr):
    return min(arr)

print(min_num([1,2,3,4]))




