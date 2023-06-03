fNum = int(input("Input first number: "))
opr = input("+-*/%: ")
sNum = int(input("Input Second number: "))

if opr == "+":
    print(fNum + sNum)
elif opr == "-":
    print(fNum - sNum)
elif opr == "*":
    print(fNum * sNum)
elif opr == "/":
    print(fNum /sNum)
elif opr == "%":
    print(fNum % sNum)
else:
    print("You put something wrong DATA")