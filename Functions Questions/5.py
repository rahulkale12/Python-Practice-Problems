#5.Create a Function That Accepts a List and Returns the Largest Element in It:

def Maximum(arr):
    if len(arr)==0:
        return arr
    largest = 0
    for i in arr:
        if i>largest:
            largest = i
    return largest
arr = [1,2,3,4,5]
print(Maximum(arr))

    
#with in built max function

def maximum(arr):
    return max(arr)

print(maximum([1,2,3,4]))