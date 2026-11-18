# class Animal:  #Parent class
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print("i dont eat", self.name)
    
# class Dog(Animal): #Child class
#     pass

# Dog1 = Dog("Cat")

# print(Dog1.name)
# Dog1.eat()


class Animal:
    def eat(self):
        print("This animal eats food")


class Dog(Animal):
    def bark(self):
        print("Woof! Woof!")


dog1 = Dog()

dog1.eat()
dog1.bark()