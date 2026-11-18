class Animal: #parent class, it receive names & stores 
    def __init__(self,name):
        self.name = name
class Dog(Animal): #this inherite from parent class
    def __init__(self, name, breed):
        super().__init__(name) #calls the parent init method
        self.breed = breed #creates a new attributes belonging to Dog object
dog1 = Dog("Prosper", "German")

print(dog1.name)
print(dog1.breed)
print()