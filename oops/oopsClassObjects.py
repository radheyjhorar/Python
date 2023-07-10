
class car:
    name = "Volvo"
    model = 2023
    sheater = 4
    color = ["White", "Black", 'Gray', 'Red']
    def update(self, name):
        self.name = name
        
    def display(self):
       print(self.name)
        
        
c = car()

# c.display()
# c.name = "bms"
# c.display()
# c.update("Audi")
# print(c.name)
# c.display()





class car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
    
    def show(self):
        print("model is ", self.model)
        print("color is ", self.color)
        
audi = car("audi a4", "blue")
ferrari = car("ferrari 488", "green")

audi.show()
ferrari.show()

print("Model of audi is", audi.model)
print("Color of ferrari is", ferrari.color)