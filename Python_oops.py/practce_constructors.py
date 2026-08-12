# pass the names and cgpa of student in constructors:
class student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

stud1 = student("vishnu",9.1)
stud2 = student("Urvashi",9.2)
print(stud1.name,stud1.cgpa)
print(stud2.name,stud2.cgpa)
