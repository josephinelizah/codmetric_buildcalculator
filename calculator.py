import math  # for square root

History = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

def modulus(a, b):
    return a % b

def exponential(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Cannot take square root of negative number"
    return math.sqrt(a)

while True:
    print("\n--- Simple Calculator ---")
    print("Choose an operation: +  -  *  /  %  **  sqrt")
    print("Type 'History' to see past calculations")
    print("Type 'Exit' to quit")

    operation = input("Enter operation: ").strip()

    if operation == "Exit":
        print("End")
        break

    if operation == "History":
        if History:
            print("\nCalculation History:")
            for item in History:
                print(item)
        else:
            print("No history yet.")
        continue

    if operation not in ["+", "-", "*", "/", "%", "**", "sqrt"]:
        print("Invalid operation. Please try again.")
        continue

    try:
        if operation == "sqrt":
            num = float(input("Enter number: "))
            result = square_root(num)
            calculation = f"sqrt({num}) = {result}"
        else:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if operation == "+":
                result = add(num1, num2)
            elif operation == "-":
                result = subtract(num1, num2)
            elif operation == "*":
                result = multiply(num1, num2)
            elif operation == "/":
                result = divide(num1, num2)
            elif operation == "%":
                result = modulus(num1, num2)
            elif operation == "**":
                result = exponential(num1, num2)

            calculation = f"{num1} {operation} {num2} = {result}"

        print("Result:", calculation)
        History.append(calculation)

    except ValueError:
        print("Invalid input. Please enter numbers only.")
