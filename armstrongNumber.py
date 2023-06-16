a = input("Enter a number: ")
s = 0
b = a
l = len(a)
for digit in a:
    s += int(digit) ** l

a = int(a)
if a == s:
   print(a,"is an Armstrong number")
else:
   print(a,"is not an Armstrong number")