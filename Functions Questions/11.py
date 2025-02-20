#11.Write a Function to Check if a Year is a Leap Year:

def leap_year(year):
    if (year % 4 == 0 and year%100!=0) or (year%400 == 0):
        return True
    return False
year = 2027
print(leap_year(year))