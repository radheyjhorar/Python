# Tow lists sum put in third list
fl = [1, 2, 3, 4, 5, 6, 71, 13, 10]
sl = [9, 6, 0, 26, 7, 8, 3, 2, 1]
total = []

if len(fl) == len(sl):   
    for i in range(len(fl)):
        total.append(fl[i] + sl[i])
print(total)    
