def armstrongNumber(value):
    a = value
    s = 0
    l = len(a)
    for digit in a:
        s += int(digit) ** l
    a = int(a)
    if a == s:
        return a, "is an Armstrong number"
    else:
        return a, "is not an Armstrong number"
    
def buzzNumber(value):
    a = int(value)
    if a % 7 == 0 or a % 10 == 7:
        return a," Is a Buzz Number"
    else:
        return a, " Is not a Buzz Number"
    
def evenOrOdd(value):
    a = int(value)
    if a % 2 == 0:
        return a, "is Even Number"
    else:
        return a, "is Odd Number"
    
def factorialNo(value):
    a = int(value)
    b = 0
    while a >= 1:
        b += a
        a -= 1
        c = a
    return "Factorial number is: ", b

    
    
value = input("Enter a Number: ")
while True:
    print("1. Armstrong Number")
    print("2. Buzz Number")
    print("3. Number is Even Or Odd")
    print("4. Factorial Number")
    print("5. Exit")
    inputOption = int(input("Choose any one Option What do you want: "))
    if inputOption >= 1 and inputOption <= 5:
        if inputOption == 1:
            print(armstrongNumber(value))
            break
        elif inputOption == 2:
            print(buzzNumber(value))
            break
        elif inputOption == 3:
            print(evenOrOdd(value))
            break
        elif inputOption == 4:
            print(factorialNo(value))
            break
        elif inputOption == 5:
            break

