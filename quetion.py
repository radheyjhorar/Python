# Input two str print concatnet both str
l1 = "Hello"
l2 = "World"
l3 = l1 + " " + l2
print(l3)

# input a string print one by one charcter reverse
str = "Hello World"
print(str[::-1])

rStr = []
l = len(str) - 1
while l >= 0:
    rStr.append(str[l])
    l -= 1
print(rStr)




# input two string and find a subString
str1 = "Hello world how are you"
str2 = "Hi guys what's going on"
print(str1.find("gjgh"))
print(str2.find("H"))

