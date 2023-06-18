# Tuples are used to store multiple items in a single variable. 
# Tuple is one of 4 built-in data types in Python used to store collections of data
# A tuple is a collection which is ordered and unchangeable.


# t = [11, 21, 33, 44, 56, 61, 7, 83, 95, 10, 151, 12]
# print(t[1])
# print(t[0:5])
# print(type(t))
# t1 = tuple(t)
# print(type(t1))
# print(t1)
# print(t1[0:5])

# for i in range(0, len(t)):
#     print(t1[i])



# a = (1, 2)
# b = (3, 90, 123, 97, 98, 41, 5, 16, 71, 899)
# c = a + b 
# print(c)
# d = a * 2
# print(d)

# f = ("Hello")
# e = f * 2
# print(e)

# print(len(f))

# print(max(f))
# print(max(b))
# print(min(f))
# print(min(b))

# # tuple(seq)
# print(tuple(b))
# # sorted(reverse = true)
# print(sorted(b))


x = ("d", "f", "g", "h", "r", "w", "e", "q", "b", "x", "z", "o", "p", "y")
y = sorted(x)
print(y)
yr = sorted(x, reverse = True)
print(yr)