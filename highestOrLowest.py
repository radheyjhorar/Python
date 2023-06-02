#Highest Number Between Three

a = 211.9
b = 5
c = 99
highestNumber = 0

if a > b and a > c:
    highestNumber = a
if b > a and b > c:
    highestNumber = b
if c > b and c > a:
    highestNumber = c

print(highestNumber)

#Lowest Number Between Three

d = 211.9
e = 5
f = 99
lowestNumber = 0

if d < e and d < f:
    lowestNumber = d
if e < d and e < f:
    lowestNumber = e
if f < e and f < d:
    lowestNumber = f

print(lowestNumber)

print(type("10"))