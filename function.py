# 1. No arguementand No return
    # def fn():
        # a = input(--------)
        # ---------
        # ---------
        # print(a)
def armNo():
    a = input("Enter a number: ")
    s = 0
    l = len(a)
    for digit in a:
        s += int(digit) ** l
    a = int(a)
    if a == s:
        print(str(a) + " is an Armstrong number")
    else:
        print(str(a) + " is not an Armstrong number")
armNo()

        
# 2. Arguementand and No return
    # def fn(arg1, arg2, arg3):
        # ---------
        # ---------
        # ---------
        # print(--)
value1 = input("Enter a number: ")      
def armNo(value1):
    a = value1
    s = 0
    l = len(a)
    for digit in a:
        s += int(digit) ** l
    a = int(a)
    if a == s:
        print(str(a) + " is an Armstrong number")
    else:
        print(str(a) + " is not an Armstrong number")
armNo(value1)


        
# 3. No Arguementand and return
    # def fn():
        # ---------
        # ---------
        # ---------
        # return -----
def armNo():
    a = input("Enter a number: ")
    s = 0
    l = len(a)
    for digit in a:
        s += int(digit) ** l
    a = int(a)
    if a == s:
        return str(a) + " is an Armstrong number"
    else:
        return str(a) + " is not an Armstrong number"
print(armNo())


# 4. Arguement and return
    # def fn(arg1, arg2):
        # ---------
        # ---------
        # ---------
        # return -----

def armstrongNumber(value):
    a = value
    s = 0
    l = len(a)
    for digit in a:
        s += int(digit) ** l
    a = int(a)
    if a == s:
        return str(a) + " is an Armstrong number"
    else:
        return str(a) + " is not an Armstrong number"


def buzzNumber(value):
    a = int(value)
    if a % 7 == 0 or a % 10 == 7:
        return str(a) + " Is a Buzz Number"
    else:
        return str(a) + " Is not a Buzz Number"


def evenOrOdd(value):
    a = int(value)
    if a % 2 == 0:
        return str(a) + "is Even Number"
    else:
        return str(a) + "is Odd Number"


def factorialNo(value):
    a = int(value)
    factorial = 1
    if a < 0:
        return "Sorry, factorial does not exist for negative numbers"
    elif a == 0:
        return "The factorial of 0 is 1"
    else:
        for i in range(1, a + 1):
            factorial = factorial*i
        return "The factorial of "+ str(a) + " is " + str(factorial)


while True:
    value = input("Enter a Number: ")
    print("1. Armstrong Number")
    print("2. Buzz Number")
    print("3. Number is Even Or Odd")
    print("4. Factorial Number")
    print("5. Exit")
    inputOption = int(input("Choose any one Option What do you want: "))
    if inputOption >= 1 and inputOption <= 5:
        if inputOption == 1:
            print(armstrongNumber(value))
        elif inputOption == 2:
            print(buzzNumber(value))

        elif inputOption == 3:
            print(evenOrOdd(value))

        elif inputOption == 4:
            print(factorialNo(value))

        elif inputOption == 5:
            break

