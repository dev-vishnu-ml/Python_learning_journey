class student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa

    def getname(self):
        return self.name

stud1 = student("Urvashi",9.2)

print(f"{stud1.getname()} and has cgpa = {stud1.cgpa}")
