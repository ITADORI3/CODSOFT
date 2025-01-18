def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Error! Division by zero is not allowed.'
    else:
        return x / y

while True:
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    # Take input for operation choice
    operation = input("Enter operation number (1/2/3/4/5): ")

    if operation == '5':
        print("Exiting the calculator program. Goodbye!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        print("Result:", add(num1, num2))
    elif operation == '2':
        print("Result:", subtract(num1, num2))
    elif operation == '3':
        print("Result:", multiply(num1, num2))
    elif operation == '4':
        print("Result:", divide(num1, num2))
    else:
        print("Invalid input")
