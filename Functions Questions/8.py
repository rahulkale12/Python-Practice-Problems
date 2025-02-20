#8.Write a Function That Returns the Sum of All Even Numbers in a List:


def sum_even_num(arr):
    return sum([x for x in arr if x%2==0])

print(sum_even_num([1,2,3,4,5,6]))



#second way

def sum_num(arr):
    sum = 0
    for x in arr:
        if x%2==0:
            sum+=x
    return sum

print(sum_num([1,2,3,4,5,6]))