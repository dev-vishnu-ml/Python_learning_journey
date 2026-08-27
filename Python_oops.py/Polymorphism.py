# polymorphism (Many forms)
class Student:
    def role(self):
        print("Study in college")

class Employee:
    def role(self):
        print("write code in The office")

class Customer:
    def role(self):
        print("customer in the market")

def describe_roles(obj):
    obj.role()

student = Student()
employee = Employee()
customer = Customer()

describe_roles(student)
describe_roles(employee)
describe_roles(customer)