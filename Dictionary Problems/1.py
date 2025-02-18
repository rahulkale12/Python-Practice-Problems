#1.Create a Dictionary to Store Student Names as Keys and Their Marks as Values, Then Display the Student with the Highest Marks:

students = {"rahul":98,"tejas": 87,"ankush":77,"sahil":76}
name = max(students , key = students.get)
print(name, students[name])