# Single Inheritance: 

class Parent:
    
    def func1(self):
        print("This function in parent class")
    
class Child(Parent):
    
    def func2(self):
        print("This function in child class")
        
        
obj1 = Child()

obj1.func1()
obj1.func2()



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
    
obj1 = Hisfriend()
obj1.print_name()