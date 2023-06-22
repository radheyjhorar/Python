# Python String Methods

# Python has a set of built-in methods that you can use on strings.

# Note: All string methods returns new values. They do not change the original string.

# built in function string

string = "Radhey Jhorar"
intezer = 50
flt = 2.47
boolean = True

# str.isalpha()
a = "radheyjhorar"
print(a + " Is alpha = " + str(a.isalpha())) #its true
a = "radhey121"  
print(a + " Is alpha = " + str(a.isalpha())) #its false


print()
# str.isdigit()
b = "1212"
print(b + " Is digit = " + str(b.isdigit()))
b = "1212radhey"
print(b + " Is digit = " + str(b.isdigit()))


print()
# len(str)
c = "radhey12390"
print("Lenght Of " + c + " is " + str(len(c)))


print()
# .split(',') The split() method splits a string into a list.
d = "Hello world, my name is Radhey, i am 23 years old"
print("split a str-var to list = " + str(d.split()))



print()
# .lower()
e = "HELLO WORLD"
print(e + " To Lower " + e.lower())



print()
# .upper()
l = "hello world"
print(l + " To Upper " + l.upper())



print()
# .islower() For cheak Is lower or not
f = "'hello world'"
print(f + " Is lower True Or False = " + str(f.islower()))
f = "'Radhey Jhorar'"
print(f + " Is lower True Or False = " + str(f.islower()))


print()
# .isupper() to cheak Is upper True Or False
g = "'Radhey Jhorar'"
print(g + " Is UPPER True Or False = " + str(g.isupper()))
g = "'HELLO WORLD'"
print(g + " Is UPPER True Or False = " + str(g.isupper()))



print()
# .replace("old", "new")
h = "hello world, my name is 'Ram'"
print("Replace = " + h + " = " + h.replace("Ram", "Radhey"))


print()
# str.find("h") It is return index number. If puted value by us is false it's return -1
i = "hello, my name is Peter, I am 26 years old"
fi = "'old'"
print(fi + " Index Number is = " + str(i.find(fi)))


print()
# str.lstrip()      Removes any leading characters(space is the default leading character) from left.
fruits = "    Banana, Mango, Kiwi     "
print(".lstrip the fruits = (" + fruits + ") = (" + fruits.lstrip() + ")")
# str.lstrip("Charcter")
fruits = "Banana, Mango, Kiwi" 
print(".lstrip the fruits = (" + fruits + ") = (" + fruits.lstrip("Banana, ") + ")")



print()
# str.rstrip()      it's like to oposite .lstrip = rstrip
names = "    Mohan, Ankit, Rahul, Naveen     "
print(".rstrip the names = (" + names + ") = (" + names.rstrip() + ")")
# str.rstrip("Charcter")
names = "Mohan, Ankit, Rahul, Naveen" 
print(".rstrip the names = (" + names + ") = (" + names.rstrip(", Naveen") + ")")


print()
# str.isspace()  it's return true Or false
j = "       "
print("In (" + j + ") all are Spaces True Or False = " + str(j.isspace()))
j = "   Radhey   "
print("In (" + j + ") all are Spaces True Or False = " + str(j.isspace()))


print()
# str.istitle()     it's returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.  Symbols and numbers are ignored.
k = "Hello World, How Are You Guys"
print("(" + k + ") In this All word are title true or false = " + str(k.istitle()))
k = "Hello world"
print("(" + k + ") In this All word are title true or false = " + str(k.istitle()))
k = "RADHEY JHORAR"
print("(" + k + ") In this All word are title true or false = " + str(k.istitle()))



# List function (built in function)
    # sum(ln)
    # list(sequence)

# Built in method | 
    # l1 = [1, 2, 3, 4]
    # l1.append(10) = [1, 2, 3, 4, 10]
    # l1.index(4) = 3
    # l1.insert(2, 11) = [1, 2, 11, 3, 4, 10]
    # l1.sort() = by defaul ascending = [1, 2, 3, 4, 10, 11]
    # l1.remove(3) = [1, 2, 4, 10, 11]
    # l1.reverse() = [11, 10, 4, 2, 1]
    # l1.count(4) = 1 (4 is one time in list)
    # l2 = [12, 13, 14, 15, 16, 17, 28] 
    # l1.extend(l2) = [11, 10, 4, 2, 1, 12, 13, 14, 15, 16, 17, 28] (The extend() method adds the specified list elements (or any iterable) to the end of the current list.)
    
    
# List comprehension
    # List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
    # New List Name = [Expresion for i in list if condition]
    # nList = [1*1 for i in l1 if i % 2 == 0]
# l1 = [12, 21, 1, 11, 2, 22]



# List Slice 
    # List[start:end:step]
# l1[21: 1: 1]
    
    
# Nested list
    # L1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # L1 = L1[0][1] = 2
    
