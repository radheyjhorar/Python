num = int(input("Enter a Number: "))
if num % 7 == 0 or num % 10 == 7:
    print(str(num) + " Is a Buzz Number")
else:
    print(str(num) + " Is not a Buzz Number")