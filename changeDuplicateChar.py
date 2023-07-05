# change string's first charcter's duplicate to $

# def changeDuplicateCharacter(str, charChange):

def charFreq(str):
    str = str.lower()
    list1 = []
    for i in str:
        if i in list1:
            list1.append("$")
        else:
            list1.append(i)
    return list1
str = "Hello world how are you"
print(charFreq(str))
    