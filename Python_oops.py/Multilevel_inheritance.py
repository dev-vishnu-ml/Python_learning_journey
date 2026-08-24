# Multilevel inheritance 
# Grandparent->parent->child
class Employee:
    start_time = "10am"
    end_time  = "5pm"

class Adminstaff(Employee):
    def __init__(self,role):
        self.role = role

class Accounts(Adminstaff):
    def __init__(self,salary,role):
        # super means Adminstaff ke init method mein role mein assign kar do
        super().__init__(role) #super is used to call the parent class method from child class
        self.salary = salary

acc1 = Accounts(50_000,"CA")
print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)