#4.Use a Lambda Function with filter() to Filter Out All Even Numbers from a List:

numbers = [1, 2, 3, 4, 5, 6]

z = (filter(lambda x:x%2==0, numbers))
print(list(z))
