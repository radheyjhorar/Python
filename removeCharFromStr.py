# remove a character from given string

def removeCharFromStr(str, rChar):
    str1 = str
    charThatRemove = rChar
    indexNo = str1.find(charThatRemove)
    str2 = str1[0:indexNo] + str1[indexNo + 1::]
    return str2
str = "Hello  world"
removeChar = " "
print(removeCharFromStr(str, removeChar))

#print(str1.replace(" ", ""))
