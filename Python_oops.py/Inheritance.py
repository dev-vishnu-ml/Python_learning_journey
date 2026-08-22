class Employee: #parent/base class
    starting_time = "10am"
    ending_time = "5pm"
    def change_end_time(self,new_time):
        self.ending_time = new_time

class Teacher(Employee): # child class inherit properties of parent class
    def __init__(self,subject):
        self.subject = subject

class Adminstaff(Employee):
    def __init__(self,role):
        self.role = role

t1 = Teacher("Maths")
t1.change_end_time("6pm")  #access the methods 
print(t1.subject,t1.starting_time,t1.ending_time) 

staff1 = Adminstaff("Manager")
print(staff1.role,staff1.starting_time,staff1.ending_time)