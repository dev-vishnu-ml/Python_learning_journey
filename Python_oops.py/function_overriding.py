# basically two type of polymorphism in python 1.function overriding 2.Duck Typing
# 1.function overriding

class Employee:
    def get_designation(self):
        print("designation  = Empoyee")

class Teacher(Employee):
    def get_designation(self): #function overriding
        print("designation = Teacher ")

teacher = Teacher()
teacher.get_designation()