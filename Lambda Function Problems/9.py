#9.Write a Lambda Function to Check if a Number Is Divisible by Both 3 and 5:

z = lambda x : x%3==0 and x%5==0
print(z(75))