a = 0
b = 1
c = 0
for i in range(0, 10):
    c = a + b
    a = b 
    b = c
    print(c)