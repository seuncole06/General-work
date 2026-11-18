class Student:
    school = "Bright Future School"

    def __init__(self, name):
        self.name = name

student1 = Student("Seun")
student2 = Student("David")

print(student1.school)
print(student2.school)