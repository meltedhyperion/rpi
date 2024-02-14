def arithmetic_operations(a, b):
    print(f"Addition of {a} and {b} is: {a + b}")
    print(f"Subtraction of {a} and {b} is: {a - b}")
    print(f"Multiplication of {a} and {b} is: {a * b}")
    if b != 0:
        print(f"Division of {a} and {b} is: {a / b}")
    else:
        print("Division by zero is not allowed")


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
arithmetic_operations(a, b)
