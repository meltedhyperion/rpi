def check_speed(speed):
    if speed < 70:
        print("OK")
    else:
        points = (speed - 70) // 5
        if points > 12:
            print("License suspended")
        else:
            print(f"Points: {points}")


speed = int(input("Enter speed: "))
check_speed(speed)
