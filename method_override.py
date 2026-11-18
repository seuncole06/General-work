class Animal:
    def sound(self):
        print("Animals different sound")

class Dog(Animal):  #A child class providing its own version of an inherited method
    def sound(self):
        print("Dogs love to bark")

class Cat(Animal):
    def sound(self):
        print("Cat love to meow")
    
class Cow(Animal):
    def sound(self):
        print("cows eat grass")

dog1 = Dog()
cat1 = Cat()
cow1 = Cow()

dog1.sound()
cat1.sound()
cow1.sound()

#Note you can print the parent message by using the supper() method but without that python will overide and print the child classes since the parent and the child have same function def sound()
