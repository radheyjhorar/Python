#Highest Number Between Three

a = -2
b = -20
c = 20
highestNumber = 0

if a > b:
    if a > c:
        print(a,"Is largest number")
    elif a == c:
        print("A and C Are equel")
    else:
        print(c,"Is largest number")
elif b > a:
    if b > c:
        print(b,"Is largest number")
    elif b == c:
        print("B and C Are equel")
    else:
        print(c,"Is largest number")
else:
    print("Numbers are equel")

#Lowest Number Between Three

# d = 211.9
# e = 5
# f = 99
# lowestNumber = 0

# if d < e and d < f:
#     lowestNumber = d
# if e < d and e < f:
#     lowestNumber = e
# if f < e and f < d:
#     lowestNumber = f

# print(lowestNumber)

# print(type("10"))