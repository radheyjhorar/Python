dayNumber = int(input("Please Enter week Number: "))

if dayNumber <= 7:
    if dayNumber == 1:
        print("Monday")
    elif dayNumber == 2:
        print("Tuesday")
    elif dayNumber == 3:
        print("Wednesday")
    elif dayNumber == 4:
        print("Thursdau")
    elif dayNumber == 5:
        print("Friday")
    elif dayNumber == 6:
        print("Saturday")
    elif dayNumber == 7:
        print("Sunday")
    else:
        print("Please enter a week number")
else:
    print("Please enter a week number")