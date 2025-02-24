#1.Create a base class Person with attributes name and age. Create a Student class that inherits Person and adds student_id.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name:{self.name} and age is:{self.age}")

class Student(Person):                               #single inheritance
    def __init__(self,name,age,student_id):
        super().__init__(name,age)     #super to access constructor method
        self.student_id = student_id

    def display_student(self):
        self.display()
        print(f"Student id : {self.student_id}")

s1 = Student("Rahul",25,1)
s1.display_student()