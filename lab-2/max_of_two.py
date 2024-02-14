def max_of_two(a, b):
    if a > b:
        return a
    else:
        return b


a = int(input("Enter a: "))
b = int(input("Enter b: "))
print(f"The maximum of a and b is: {max_of_two(a, b)}")
