# methods-> class,static,instance method 

class student:
    college_name = "abc college"
    def __init__(self,student_name,cgpa):
        self.student_name = student_name
        self.cgpa = cgpa
    @classmethod    
    def get_college_name(cls):
        print(f"college name is: {cls.college_name}")

    @staticmethod
    def get_fees_discount(fees,discount):
        final_fees = fees -(discount*fees/100)
        print(f"the final dicounted price: {final_fees}")

    def get_info(self):
        print(f"name is: {self.student_name} and cgpa is {self.cgpa} and college: {self.college_name}")

student1 = student("xyz",8.4)
student1.get_college_name()
student1.get_fees_discount(45300,10)