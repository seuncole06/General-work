class Students:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("I am", self.age, "years old")

Students1 = Students("seun", 23)
Students2 = Students("daniel", 30)
Students3 = Students("cole", 11)

Students1.introduce()
Students2.introduce()
Students3.introduce()

