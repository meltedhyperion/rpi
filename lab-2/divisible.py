def divisible(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Three and Five"
    elif num % 3 == 0:
        return "Three"
    elif num % 5 == 0:
        return "Five"

    else:
        return num


num = int(input("Enter a number: "))
print(f"The number is divisible by: {divisible(num)}")
