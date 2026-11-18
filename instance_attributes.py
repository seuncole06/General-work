class Phone:
    brand = "Samsung" #class attributes 

    def __init__(self, model, price):
        self.model = model #instance attributes
        self.price = price #instance attributes

phone1 = Phone("Galaxy S25", 800000)
phone2 = Phone("Galaxy A16", 250000)

print(phone1.brand)
print(phone2.brand)

print(phone1.model)
print(phone2.model)
print(phone1.price)
print(phone2.price)