age = int(input("Enter your age: "))
has_id_card = input("Do you have an ID?, (yes/no): ")

if age >= 18 and has_id_card == "yes":
    print("Acess granted")
else:
    print("Acess denied")
