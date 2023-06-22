# Types of arguement

    # 1. Positional arguement
    
def greet(name, deft):
    print("Hi " + name)
    print("Are you from " + deft + " department?")
#greet("CS", "Radhey")



    # 2. Default arguement
    
def gr(name, subject, dept="CS"):
    print("Hi " + name)
    print("Do you teach " + subject + "?")
    print("Are you from " + dept + " department?")
# gr("Radhey", "Python")
# gr("Radhey", "Python", "ME")
    
    
    
    # 3. Keyword/Name arguement
    
def grt(name, deft):
    print("Hi " + name)
    print("Are you from " + deft + " department?")
#grt(deft="CS", name="Radhey")  
    
    
    # 4. Variable length arguement
    
def add(*numbers):  # its creat a tupel
    c = numbers
    print(type(c))
    d = 0
    for i in numbers:
        d += i
    print("Sum is " + str(d))
add(5,7,6,9)
add(5,7,6,9,66,244, 10)