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



def getSum(n):
    
    sum = 0
    for digit in str(n): 
      sum += int(digit)      
    return sum
   
n = int(input("Enter a number: "))
print(getSum(n))