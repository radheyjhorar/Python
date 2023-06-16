# count lowercase later and uppercase later
a = 'Hello World'
u = []
l = []
for digit in a:
    d = ord(digit)
    if d >= 65 and d <= 90:
        u.append(chr(d))
    elif d >= 97 and d <= 122:
        l.append(chr(d))
print(u, "This is upper Digits", "Total Digits = ", len(u))
print(l, "This is lower Digits", "Total Digits = ", len(l))