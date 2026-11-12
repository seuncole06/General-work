# # name = input("What is your name? ")

# # print(name)

# # name = input("Enter your name: ")
# # age = input("Enter your age: ")

# # print("Name:", name)
# # print("age:", age)
# # age = int(input("Enter you age: "))

# # if age >= 18:
# #     print("Your are able to vote.")
# # else:
# #     print("You cannot vote.")

# # age = int(input("Enter your age: "))
# # has_ticket = int(input("Enter ticket number: "))

# # if age >= 18 and has_ticket >=20:
# #     print("You may enter.")
# # else:
# #     print("Entry denied")

# # def greet(name):
# #     print("Hello", name)

# # result = greet("Seun")

# # print(result)

# # milk_ounces = 16
# # pour_amount = 6
# # remaining = milk_ounces - pour_amount
# # print(remaining)
# # print(2 + 3 * 4)
# # print((2 + 3) * 4)

# # ounces = 8.5
# # print("Pouring " + str(ounces) + " ounces of milk.")

# # value1 = "15"
# # value2 = "banana"
# # print(value1.isdigit())
# # print(value2.isdigit())

# # selected_drink = "Green Tea"
# # target_temp = 100
# # if selected_drink == "Green Tea":
# #     target_temp = 80

# # print(target_temp)

# # for count in range(3):
# #     print("Grind" + str(count))

# # weight = 0.0
# # while weight < 2.5:
# #     weight = weight + 0.5
# #     print("Current weight:" + str(weight))

# # order = "   espresso  "
# # print(order.strip().upper())

# # name = "Alice"
# # drink = "latte"
# # price = 4.50

# # # The f-string automatically formats the variables inside the string
# # receipt = f"Order for {name}: {drink} — ₦{price:.2f}"
# # print(receipt)
# # sentence = "latte and espresso"
# # words = sentence.split(" and ")
# # print(words)
# # rejoined = "-".join(words)
# # print(rejoined)

# # def count_up(n):
# #     if n < 1:
# #         return[]
    
# #     result = []
# #     for i in range(1, n + 1):
# #         result.append(i)

# #     return result

# # def sum_multiples(limit, divisor):
# #     limit = (1, 10)
# #     divisor = (1, 10)

# # The function is self-contained. It only cares about the parameter variable.
# # def print_label(name):
# #     print("Name on cup: " + name)

# # # Pass the data directly into the call
# # print_label("Alice")
# # print_label("Bob")

# # def make_custom_drink(base_drink, milk_type, sugar_packets):
# #     # Assemble the descriptive string step-by-step
# #     description = f"{base_drink} with {milk_type} milk"
    
# #     if sugar_packets > 0:
# #         description = description + f" and {sugar_packets} sugar packets"
        
# #     return description

# # # Generate distinct order strings
# # order1 = make_custom_drink("Latte", "almond", 2)
# # order2 = make_custom_drink("Cappuccino", "whole", 0)

# # print(order1) # "Latte with almond milk and 2 sugar packets"
# # print(order2) # "Cappuccino with whole milk"

# # def clean_stack(mugs):
# #     if mugs <= 0:
# #         return
    
# #     print("Cleaning...")
# #     clean_stack(mugs- 1)

# # def fix_greeting(name):
# #     # Bug to fix: the function should use name, not an undefined variable.
# #     name = "Ada"
# #     fix_greeting =("Hello," + {name})
# #     return(fix_greeting)

# # def get_item(items, index):
# #     # Bug to fix: invalid indexes should not crash the program.
# #     if index < 0:
# #         return "Index out of range."
# #     get_item = list(items[index])
# #     if index != list:
# #      return "Index out of range"
# #     return get_item 

# # flavors = ["vanilla", "Caramel", "Hazeinut"]
# # flavors.sort()
# # print(flavors)

# # student = {
# #     "name": "Seun",
# #     "age": 25,
# #     "city": "Lagos"
# # }

# # print(student)

# # items = {"Cocoa", "Cocoa", "Vanilla"}
# # print(items)
# # print(len(items))

# # specials_tray = {"Cinnamon", "Cocoa", "Vanilla"}

# # # Safely check membership
# # if "Cinnamon" in specials_tray:
# #     print("Sprinkling cinnamon on the drink...")

# # toppings = {"Cinnamon", "Cocoa"}
# # print("Cinnamon" in toppings)
# # print("Nutmeg" not in toppings)

# # numbers = {1, 2, 3}

# # numbers.clear()

# # print(numbers)

# # def get_choices():
# #     seun_cole   = "star"
# #     computer_choice = "paper"

# #     return computer_choice

# # choices = get_choices()
# # print(choices)

# # class KioskMachine:
# #     pass

# # print(KioskMachine)

# # class CoffeeCup:
# #     def __init__(self, size, owner):
# #         self.size = size  # "self" binds the data to the specific object
# #         self.owner = owner

# # # Create a cup, passing values for size and owner
# # alice_cup = CoffeeCup("large", "Alice")
# # print(alice_cup)

# # class Student:
# #     pass

# # student1 = Student()

# # student1.name = "Seun"

# # first_name = "seun"
# # last_name = "cole"
# # full_name = first_name + " " + last_name

# # print(full_name)
# # print(type(full_name))

# # age = 20
# # age += 2

# # print(age)
# # print(type(age))

# # height = 200.5
# # print("your height is : "+str(height))
# # print(type(height))

# # human = True
# # print("Are you a human: "+str(human))
# # print(type(human))

# # name = "cole"
# # # age = 20
# # # attractive = True
# # # name, age, attractive = "cole", 20, True

# # print(name.count("e"))
# # # print(age)
# # # print(attractive)

# # x = 1
# # y = 2.0
# # z = "3"

# # y = int(y)
# # print(x)
# # print(y)
# # print(z)

# # name = input("what is your name?: ")
# # age = int(input("how old are you"))

# # print("Hello "+ name)
# # print("You are "+ str(age)+ " years old")

# # import math

# # pi = 420

# # print(math.sqrt(pi))

# # temp = int(input("what is the temp outside?: "))

# # if temp >=0 and temp <= 30:
# #     print("you can go outside")
# # elif temp < 0 or temp > 30:
# #     print("you cant go outside")

# # if not(temp >=0 and temp <= 30):
# #     print("you can go outside")

# # rows = int(input("How many rows?: "))
# # columns = int(input("How many coumns?: "))
# # symbol = input("Enter a symbol: ")

# # for i in range(rows):
# #     for j in range(columns):
# #         print(symbol, end="")
# #     print()

# # while True :
# #     name = input("Enter your name: ")
# #     if name != "":
# #         break

# # for i in range(1, 21):
# #     if i == 13:
# #         pass
# #     # else:
# #     #     print(i, end="")

# # student = ("Cole", 21, "male")
# # print(student)

# # untensils = {"cole", "prosper", "alfa", "yvette"}
# # dishes = {"spoon", "bowl", "plate"}

# # untensils.update(dishes)

# # for x in untensils:
# #     print(x, end="")

# # name = "seun cole"

# # if (name[1].islower()):
# #     name = name.capitalize()

# # print(name)

# # def hello(first,middle,last):
# #     print("hello "+first+" "+middle+" "+last)

# # hello("sam","col","deb")
    
# # def hello(**cole):
# #     print("hello",end=" ")
# #     for key, value in cole.items():
# #             print(value,end=" ")

# # hello(first="Bro", middle="Dude", last="code")

# # print('My favorite color is, blue, green, red')

# # import random

# # x = random.randint(1,6)
# # y = random.random()
# # print(y)
# # my_list = ['blue', 'green', 'red', 'black']
# # z = random.choice(my_list)

# # print(z)

# # try:
# #     numerator = int(input("Enter a number to divide: "))
# #     denumerator = int(input("Enter a number to divide: "))
# #     result = numerator / denumerator
# #     print(result)
# # except ZeroDivisionError:
# #     print("You cant divide by zero")
# # except ValueError:
# #     print("Enter only number")
# # except Exception:
# #     print("cant work")
# # else:
# #     print(result)

# # import os

# # path = "//home//gamp//Desktop//test.txt"

# # if os.path.exists(path):
# #     print("The location exist")
# # if os.path.isfile(path):
# #     print("it is a file")
# # else:
# #     print("Doesn't exist")

# # text = "my name is cole\nI love to code\nArsenal for life\n"

# # with open("test.txt","w") as file:
# #     file.write(text)

# # import os

# # source = "test.txt"
# # destination = "//home//gamp//test.txt"

# # try:
# #     if os.path.exists(destination):
# #         print("file already acailable")
# #     else:
# #         os.replace(source,destination)
# #         print(source+" was moved")
# # except FileExistsError:
# #     print(source+" was not found")

# # import os

# # path = "//home//gamp//test.txt"

# # try:
# #     os.remove(path)
# # except FileNotFoundError:
# #     print("file not found")

# # result = pow(2, 3)
# # print(result)

# # def new_game():

# # def greet():
# #     message = 'Hello!'
# #     print(message)

# # greet()
# # print(message)

# # for row in range(3):
# #     for star in range(4):
# #         print("*", end=" ")
# #     print()

# # for i in range(4):
# #     for j in range(2):
# #         print(i, j)

# # items = ["pen", "book", "bag", "cup"]
# # for item in items:
# #     print("Hello")

# # def binary(nums, target):
# #     first = 0
# #     last = len(nums)-1
# #     index = -1

# #     while first <= last:
# #         mid = first (last + first) // 2
    
# #         if nums[mid] == target:
# #             index = mid
# #             last = mid - 1
# #         elif nums[mid] < target:
# #             last = mid + 1
# #         else:
# #             first = mid - 1
# #     return index
# # print(binary(nums = [1, 3, 3, 3, 5, 8], 3 ))


# Roman = {
#     "I": = 1, 
#     "V": = 5, 
#     "X": = 10, 
#     "L": = 50, 
#     "C": = 100, 
#     "D": = 500 
#     "M": = 1000
#     }
# word = "length"
# new = word[1]
# print(new)


# import requests

# response = requests.get("https://example.com")

# print(response.status_code)

# file = open("students.txt", "w")

# file.write("Name: Seun")
# file.close()

# import os

# desktop = os.path.join(os.path.expanduser("~"), "Desktop")
# file_path = os.path.join(desktop, "cole.txt")

# text = "my name is cole\ni love egg"

# with open(file_path, "w") as file:
#     file.write(text)

# print("Success! Check your Desktop:", file_path)


# {
#     "name": "Seun",
#     "age": 33,
#     "country": "Nigeria"
# }

# import json

# student = {
#     "name": "Seun",
#     "age": 33,
#     "country": "Nigeria"
# }

# with open("student.json", "w") as file:
#     json.dump(student, file)


# import json

# student = {
#     "name": "seun",
#     "age": 23,
#     "lifestyle": "flexing",
#     "location": "Nigeria"
# }

# with open("student.json", "w") as file:
#     json.dump(student, file)

# with open("student.json","r") as file:
#     student = json.load(file)

#     student =["age"] = 34
#     student =["city"] ="lagos"

# with open("student.json", "")

# import json

# try: 
#     with open("student.json", "r") as file:
#         student = json.load(file)
#     print(student)
# except FileNotFoundError:
#     print("File not available")
# except json.JSONDecodeError:
#     print("File content invalid")



import json

student = [
    {"name": "seun", "age": 20, "location": "Nigeria"},
    {"name": "daniel", "age": 90, "location": "iran"}
    ]
    

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    student_saved = json.load(file)

for student in student_saved:

    print(student["name"])

new_student = {
    "name": "prosper",
    "age": 50,
    "location": "california"
}

student_saved.append(new_student)
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

with open("student.json", "r") as file:
    student_saved = json.load(file)

print(len(student))
