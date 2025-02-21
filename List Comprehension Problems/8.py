#8.Generate a List of Numbers from 1 to 100 That Are Divisible by Both 3 and 5:

z = [x for x in range(1,100) if x%3==0 and x%5==0]
print(z)