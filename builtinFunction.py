# Python Built in Functions

# int()  Returns an integer number / convert in integer
a = int(3.5)
print("Convert float to int ", a)
a = int("12")
print("convert str to int ", a)


print()
# str()      Returns a string object
    # The str() function converts the specified value into a string.
b = str(3.5)
print("Convert float to str = ", b)
b = str(12)
print("Convert integer to string = ", b)



print()
# input()     Allowing user input
    # The input() function allows user input.
    # input(prompt)     prompt = A String, representing a default message before the input.
# c = input("Enter your name:")
# print("Hello, " + c)



print()
# float()      	Returns a floating point number
    # The float() function converts the specified value into a floating point number.
    # float(value)       value = A number or a string that can be converted into a floating point number
d = float(3)
print("Convert Integer to float = ", d)
d = float("3.500")
print("Convert string to float = ", d)


print()
# eval()      Evaluates and executes an expression
        # The eval() function evaluates the specified expression,
        # if the expression is a legal Python statement, it will be executed.
        # Syntax
            # eval(expression)
                # expression = A String, that will be evaluated as Python code
            
print("eval()")
x = 'print(55)'
eval(x)
e = eval("4 + 5 * 3")
print(e)
print(eval("4 + 9 * 4"))



print()
# max()     Returns the largest item in an iterable
    # The max() function returns the item with the highest value, 
    # or the item with the highest value in an iterable.
    # If the values are strings, an alphabetically comparison is done.
f ="Mike", "John", "Vicky"
print(f)
f = max("Mike", "John", "Vicky")
print("Return the name, ordered alphabetically:", f)
print()
g = (1, 5, 3, 9, 12)
print(g)
print("Return the item in a tuple with the highest value:", max(g))



print()
# min()
    # Returns the smallest item in an iterable
    # The min() function returns the item with the lowest value,
    # The item with the lowest value in an iterable.
    # If the values are strings, an alphabetically comparison is done.
h = "Mike", "John", "Vicky"
print(h)
print("Return the name with the lowest value, ordered alphabetically:", min(h))
print()
i = (1, 5, 3, 9)
print(i)
print("Return the item in a tuple with the lowest value:", min(i))



print()
# abs()     
    # Returns the absolute value of a number
    # The abs() function returns the absolute value of the specified number.
j = -7.25
print("float Number = ", j)
print("float to abs(absolute): ", abs(j))
print()
k = 3+5j
print(k)
print("complex number to abs(absolute):", abs(k))



print()
# len()
    # Returns the length of an object
    # The len() function returns the number of items in an object.
    # string / list / tuple
mylist = ["apple", "banana", "cherry"]
print(mylist)
print("Length Of list = ", len(mylist))
print()
mylist1 = "Hello"
print(mylist1)
print("Length Of String = ", len(mylist1))
print()
mylist2 = ("Radhey", "Rahul", "Surya", "sanjay")
print(mylist2)
print("Length Of tuple = ", len(mylist2))



print()
# round(n, p)        Rounds a numbers
    # The round() function returns a floating point number that is a rounded version of the specified number,
    # with the specified number of decimals.
    # The default number of decimals is 0, meaning that the function will return the nearest integer.
    # syntax
        # round(number, digits)
            # number = Required. The number to be rounded
            # digits = Optional. The number of decimals to use when rounding the number. Default is 0
fn = 5.76543
print(fn)
print("Round a number to only two decimals:", round(fn, 2))
print("Round to the nearest integer:", round(fn))



print()
# range()
    # Returns a sequence of numbers, starting from 0 and increments by 1 (by default)
    # and stops before a specified number.
    # Syntax
        # range(start, end, step)
            # start = which position to start. Default is 0
            # stop = which position to stop (not included).
            # step = specifying the incrementation. Default is 1
rnum = range(6)
print(rnum)
print("Create a sequence of numbers from 0 to 5, and print each item in the sequence:")
for n in rnum:
    print(n)
    
print()
rnum1 = range(3, 6)
print(rnum1)
print("Create a sequence of numbers from 3 to 5, and print each item in the sequence:")
for n in rnum1:
    print(n)
    
print()
rnum2 = range(3, 20, 2)
print(rnum2)
print("Create a sequence of numbers from 3 to 19, but increment by 2 instead of 1:")
for n in rnum2:
    print(n)