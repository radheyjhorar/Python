# Print largest and smallest number in list
li = [12, 111, 390, 1200, 1, -1, 0, -7, 3900, 500878]
print("Smallest Number = ", min(li))
print("Largest Number = ", max(li))

larg = li[0]
small = li[0]
for num in li:
    if num > larg:
        larg = num
    elif num < small:
        small = num
print("Largest Number = ", larg)
print("smallest Number = ", small)