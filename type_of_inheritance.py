# #Single inheritance
# class Animal: #parent 
#     def eat(self):
#         print("eat food")

# class Dog(Animal): #child inherite from only parent
#     pass

# dog1 = Dog()

# dog1.eat()

#Multiple Inheritance
#Note - the child inherite from both father & mother 
# class Father: 
#     def drive(self):
#         print("father can drive")

# class Mother:
#     def cook(self):
#         print("mother can cook")

# class child(Father, Mother):
#     pass

# child1 = child()

# child1.drive()
# child1.cook()

# # Multilevel Inheritance
#The child can access methods from both the parent and grandparent.
# class Grandparent:
#     def house(self):
#         print("built houses")

# class parents(Grandparent):
#     def car(self):
#         print("can drive")

# class child(parents):
#     pass

# child1 = child()

# child1.house()
# child1.car()

# Hierarchical Inheritance
# Hierarchical inheritance happens when multiple child classes inherit from one parent class.

# class Animal:
#     def eat(self):
#         print("Animals can eat")

# class Dog(Animal):
#     pass

# class Cat(Animal):
#     pass

# class Cow(Animal):
#     pass

# dog1 = Dog()
# Cat1 = Cat()
# cow1 = Cow()

# dog1.eat()
# Cat1.eat()
# cow1.eat()

# Hybrid Inheritance -- Hybrid inheritance is a combination of two or more types of inheritance.
#Note --- Professor inherits from both Teacher and Researcher. Those classes both inherit from Person.
class person:
    def introduce(self):
        print("i am a person")

class Teacher(person):
    def teach(self):
        print("i teach student")

class Researcher(person):
    def research(self):
        print("i research items")

class professor(Teacher, Researcher):
    pass

professor1 = professor()

professor1.introduce()
professor1.teach()
professor1.research()