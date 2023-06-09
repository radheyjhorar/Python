# a = int(input("Enter a Number: "))
# b = a % 10
# c = a / 10
# print("Sum =",b + c)
# print("reverse =",b,c)


num = int(input("Enter a Number: "))
s = 0
for i in str(num):
    s += int(i)
print(s)