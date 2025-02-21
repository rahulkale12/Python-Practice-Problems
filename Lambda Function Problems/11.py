#11.Create a Lambda Function to check year is leap or not:


leap = [lambda year : (year%4== 0 and year%100!=0) or (year %400==0)]
print(leap(2024))


#second way using both list comprehension and lambda 

years = [2000, 2004, 1900, 2024, 2023]

leap = [year for year in years if (lambda y: (y%4==0 and y%100!=0) or (year%400==0))(year)]
print(leap)