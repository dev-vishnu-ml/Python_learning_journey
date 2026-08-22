# single inheritance
class Employee:
    starting_time = "10am"
    ending_time = "5pm"
    def change_ending_time(self,new_time):
        self.ending_time = new_time

class teacher(Employee):
    def __init__(self,subject):
        self.subject = subject

teacher1 = teacher("python")
print(teacher1.subject,teacher1.starting_time,teacher1.ending_time)
