def oddOrEven(number):
    if number % 2 == 0:
        return "EVEN"
    else:
        return "ODD"


def showNumbers(limit):
    for i in range(limit + 1):
        print(i, oddOrEven(i))


showNumbers(int(input("Enter a limit: ")))
