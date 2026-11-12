num1 = int(input("First number: "))
operator = input("Operator: ")
num2 = int(input("Second number: "))

if operator == "+":
    result = num1 + num2
    print(f"Result: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Result: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Result: {result}")
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by zero")
    else:
        result = num1 / num2
        print(f"Result: {result}")
else:
    print("Invalid operator")