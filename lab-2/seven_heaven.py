def check_number(n):
    while True:
        if n < 7:
            print(f"{n} is less than 7")
            n += 1
        else:
            print(f"{n} is not less than 7")
            break


check_number(int(input("Enter a number: ")))
