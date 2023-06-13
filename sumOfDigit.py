# a = int(input("Enter a Number: "))
# b = 0
# c = 0
# while a > 0:
#     b = a % 10
#     c += b
#     a //= 10
# print(c)



# num = int(input("Enter a Number: "))
# num1 = num
# s = 0
# for d in str(num):
#     s += int(d)
# print(s) 



num = 123
num1 = num
s = 0
for i in len(str(num)):
    digit = num1 % 10
    s += digit
    num1 //= 10
print(s)