# Multiple Inheritance

class First_class:
    a = 10
    b = 20
    def addition(self):
        print(self.a + self.b)

class Second_class:
    c = "Radhey "
    d = "Jhorar"
    def addTwoStr(self):
        print(self.c + self.d)
        
class Third_class(First_class, Second_class):
    
    def addIntStr(self):
        print(self.c + self.d, self.a+self.b)
        

# thirdClassObj = Third_class()
# thirdClassObj.addition()
# thirdClassObj.addTwoStr()
# thirdClassObj.addIntStr()


class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])
            
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)
    
    def findArea(self):
        a, b, c = self.sides
        
        s = (a + b + c) / 2
        
        area = (s*(s-a)*(s-b)*(s-c))**0.5
        print("The area of triangle is " + str(area))
        
t = Triangle()

t.inputSides()
t.dispSides()
t.findArea()
        

