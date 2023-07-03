# # Input two str print concatnet both str
# l1 = "Hello"
# l2 = "World"
# l3 = l1 + " " + l2
# print(l3)

# # input a string print one by one charcter reverse
# str = "Hello World"
# print(str[::-1])

# rStr = []
# l = len(str) - 1
# while l >= 0:
#     rStr.append(str[l])
#     l -= 1
# print(rStr)




# input two string and find a subString
# str1 = "Hello world how are you"
# str2 = "Hi guys what's going on"
# print(str1.find("gjgh"))
# print(str2.find("H"))


# cractor friquency
# a = "google.com"
# b = {}
# for i in a:
#     if(b.get(i) == None):
#         b[i] =  a.count(i) 
# print(b)

def charFreq(str):
    str = input("Input a string: ")
    count = {}
    
    for i in str:
        keys = count.keys()
        
        if i in keys:
            count[i] += 1
        else:
            count[i] = 1
    return count
#print(charFreq(str))



# List lstrip
l = [12, 20, 30, 40, 50, 60, 70]
t = 3
for i in range(t):
    fv = l.pop(0)
    l.append(fv)
#print(l)

def lstrip(l, howOften):
    t = howOften
    for i in range(t):
        fv = l.pop(0)
        l.append(fv)
    return l
l = [12, 20, 30, 40, 50]
#print(lstrip(l, 3))



# string Length
def strlen():
    a = "Radhey jhorar How are you"
    l = 0
    for i in a:
        l+=1
    return l
# print("String Length is = " + str(strlen()))