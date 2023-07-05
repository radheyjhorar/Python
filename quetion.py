# # Input two str print concatnet both str
def concatStrs(str1, str2):
    str3 = str1 + " " + str2
    return str3
str1 = "Hello"
str2 = "World"
#print(concatStrs(str1, str2))



# input a string print one by one charcter reverse
def reverseStr():
    str = input("Enter a String: ")
    print(str[::-1])
    reverseStr = []
    l = len(str) - 1
    while l >= 0:
        reverseStr.append(str[l])
        l -= 1
    return reverseStr
#print(reverseStr())




#find a subString from given string
def findSubStr(str, find):
    foundValue = str.find(find)
    return foundValue
str = "Hello world how are you"
find = "a"
#print(findSubStr(str, find))


# cractor friquency
def charFrequency(str):
    dict = {}
    for i in str:
        if(dict.get(i) == None):
            dict[i] =  str.count(i) 
    return dict
#str = input("Enter a string: ")
#print(charFrequency(str))


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