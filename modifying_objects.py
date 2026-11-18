class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print("my name is", self.name)
        print("i am", self.age, "years old")
Student1 = Student("seun", 19)
Student2 = Student("cole", 99)

Student1.city = "Lagos"
Student2.age = 86

del Student2.name

Student1.introduce()
Student2.introduce()
