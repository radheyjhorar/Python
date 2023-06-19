# 1. Bubble shorting

# ele = []
# while True:
#     t = int(input("Enter a number: "))
#     ele.append(t)
#     c = input("Enter y for continuous")
#     if c != "y":
#         break

# l = len(ele)
# print("Original list: ", ele) 
# for i in range(0, l - 1):
#     for j in range(0, l - i - 1):
#         if ele[j] > ele[j + 1]:
#             ele[j], ele[j + 1] = ele[j + 1], ele[j]

# print("List after sorting is: ", ele) 



# 2. Insertion sorting

a = [45, 67, 55, 22, 33]
n = len(a)
e = 1
print("Orignal list: ", a)
for e in a:
    g = a.index(e)
    while g > 0:
        if a[g-1] > a[g]:
            a[g-1],a[g] = a[g],a[g-1]
        g = g - 1
print("Sorted list by insertion: ", a)