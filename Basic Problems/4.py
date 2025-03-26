#4. Find the maximum number in a list.

def max_num(arr):
    max = 0
    for i in range(len(arr)):
       if i>max:
           max = arr[i]
    return max

print(max_num([1,2,3,4]))



#second way using max()
def max_num(arr):
    return max(arr)

print(max_num([1,2,3,4]))


