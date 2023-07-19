# Single Inheritance: 

class Parent:
    
    def func1(self):
        print("This function in parent class")
    
class Child(Parent):
    
    def func2(self):
        print("This function in child class")
        
        
obj1 = Child()

# obj1.func1()
# obj1.func2()


class A:
    # num1 = int(input("Enter first number: "))
    # num2 = int(input("Enter second number: "))
    
    def add(self):
        print("Addition",self.num1+self.num2)
    def sub(self):
        print("Substraction",self.num1-self.num2)
        
class B(A):
    
    def multi(self):
        print("Multiplication: ",self.num1*self.num2)
    def div(self):
        print("Devision: ",self.num1/self.num2)
    def rem(self):
        print("Remainder: ",self.num1%self.num2)


# objb = B()
# objb.add()
# objb.sub()




# Multilevel Inheritance :

class Myname:
    name1 = "Radhey"

class Myfriend(Myname):
    name2 = "Rahul"
    
class Hisfriend(Myfriend):
    name3 = "Karan"
    
    def print_name(self):
        print("My name is:", self.name1)
        print("My Friend's name is:", self.name2)
        print("My Friend's friend name is:", self.name3)
    
# obj1 = Hisfriend()
# obj1.print_name()


class Father:
    fname = "Ranjeet "
    surName = "Singh "
    
class Son(Father):
    sname = "Ravikant "        
        
class GSon(Son):
    gsname = "Ravi "
    
    def show(self):
        print("Father's Full Name: ",self.fname+self.surName)
        print("Son's Full Name: ",self.sname+self.surName)
        print("Grand Son's Full Name: ",self.gsname+self.surName)
        
# obj = GSon()
# obj.show()


class Animal:
    name = ""
    
    def eat(self):
        print("I can eat")
        
class Dog(Animal):
    
    def eat(self):
        self.eat()
        print("I like to eat Bones")
        
# labradog = Dog()

# labradog.eat()




# Method Resolution Order (MRO) in Python

class SuperClass1:
    def info(self):
        print("Super class 1 method called")
        
class SuperClass2:
    def info(self):
        print("Super class 2 method called")
        
class Derived(SuperClass1, SuperClass2):
    pass

d1 = Derived()
d1.info()