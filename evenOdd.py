# Even and Odd Number print defrent defrent list
l1 = [12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
even = []
odd = []
# i = 0
# while i <= len(l1) - 1:
#     if l1[i] % 2 == 0:
#         even.append(l1[i])
#     elif l1[i] % 2 != 0:
#         odd.append(l1[i])
#     else:
#         print('Something wrong')
#     i = i + 1
print("Even = ", even)
print("Odd = ", odd)

for i in l1:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
        