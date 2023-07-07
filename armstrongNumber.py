# Is armstrongNumber or not Function
def armStrong(num1):
   sum = 0
   num2 = num1
   for digit in num1:
      sum += int(digit) ** len(num1)
      
   num1 = int(num1)
   if num1 == sum:
      return str(num1) + " is an Armstrong number"
   else:
      return str(num1) + " is not an Armstrong number"
         
num1 = input("Enter a number: ")

print(armStrong(num1))