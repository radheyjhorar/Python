class test_constructors():
    v1 = 12
    v2 = 6
    def __init__(self, v3, v4):
        r1 = self.v1 + self.v2
        r2 = v3 + v4
        #print(r1, r2)
        
obj = test_constructors(12, 15)


class GeekforGeeks():
    
    def __init__(self):
        self.geek = "GeekforGeeks"
        
    def print_Geek(self):
        print(self.geek)
        
        
obj = GeekforGeeks()

#obj.print_Geek()

class Addition():
    first = 0
    second = 0
    answer = 0
    
    def __init__(self, f, s):
        self.first = f
        self.second = s
        
    def display(self):
        print("First Number = " + str(self.first))
        print("Second Number = " + str(self.second))
        print("Addition of tow Number = " + str(self.answer))
        
    def calculate(self):
        self.answer = self.first + self.second
        
obj1 = Addition(1000, 2000)

obj2 = Addition(10, 20)

# obj1.calculate()

# obj2.calculate()

# obj1.display()

# obj2.display()