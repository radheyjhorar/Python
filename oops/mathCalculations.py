class Calculations:
    num1 = input("Enter a number: ")
    sum = 0
    def armStrong(self):
        for digit in self.num1:
            self.sum += int(digit) ** len(self.num1)
        self.num1 = int(self.num1)
        if self.num1 == self.sum:
            return str(self.num1) + " is an Armstrong number"
        else:
            return str(self.num1) + " is not an Armstrong number"
    
    def buzzNumber(self):
        num1 = int(self.num1)
        if num1 % 7 == 0 or num1 % 10 == 7:
            return str(num1) + " Is a Buzz Number"
        else:
            return str(num1) + " Is not a Buzz Number"
        
    def calculator(self):
        fNum = int(self.num1)
        opr = input("+-*/%: ")
        sNum = int(input("Input Second number: "))
        if opr == "+":
            return fNum + sNum
        elif opr == "-":
            return fNum - sNum
        elif opr == "*":
            return fNum * sNum
        elif opr == "/":
            return fNum /sNum
        elif opr == "%":
            return fNum % sNum
        else:
            return "You put something wrong DATA"
        
    def evenOrOdd(self):
        num = int(self.num1)
        if num % 2 == 0:
            return self.num1 + " Is Even Number"
        else:
            return self.num1 + " Is Odd Number"
                
                
c = Calculations()

#print(c.armStrong())

#print(c.buzzNumber())

#print(c.calculator())

print(c.evenOrOdd())