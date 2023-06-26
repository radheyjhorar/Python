# File Heandling 
# Three types of file 
    # 1. text file
    # 2. binary file
    # 3. cvs file
# fileVariable = open("fileName", accessMode)
    # accessMode 
        # r = read
        # w = write
        # a = append
        
# FILE READING
      
# f1 = open("demofile.txt", "r")
# print(f1.read(7))
# f1.close()
# f1 = open("demofile.txt", "r")
# print(f1.read())
# f1.close()
# print()
# f1 = open("demofile.txt", "+r")
# print(f1.readlines(1))


# FILE READ WITH LOOP
# f = open("demofile.txt", "r")
# for x in f:
#   print(x) 
# f.close()



# FILE WRITING
# str = "My name is Radhey"
# f1 = open("demofile.txt", "w")
# f1.write(str)
# f1.close()

# FILE WRITE WITH LOOP
# f = open("demofile.txt", "a")
# while True:
#     str = input("Enter string: ")
#     f.write("\n" + str)
#     print("for continue press -y- for close press -c-")
#     inp = input("Y OR C: ")
#     if inp != "y":
#         break
# f.close()

# AFTER WRITE READ THE FILE
# f = open("demofile.txt", "r")
# print(f.read())




# FILE APPENDING
# f1 = open("demofile.txt", "a")
# str1 = "Hellow world what's going on \n"
# f1.write(str1)
# f1.close()
# # READ FILE AFTER APPENDING
# f1 = open("demofile.txt", "r")
# print(f1.read())
# f1.close()


# writelines(seq of lines)
# list = ["Hello world \n", "How are you \n", "My name is Radhey Jhorar \n", "can i know your name"]
# f = open("demofile1.txt", "a")
# f.writelines(list)
# f.close()

# # After writelines read file
# f = open("demofile1.txt", "r")
# print(f.read())
# f.close()


# with open file
# with open("demofile1.txt", "r") as f:
#     readf = f.read()
#     print(readf)
# no need to close file in "with open clouse"


# if we open file for write/read "w/r" and file not exists then file automatice created:
with open("test.txt", "w") as f:
    f.write("Hello world this is created automatice new file")
# print after write its file relative path
with open("test.txt", "r") as f:
    readf = f.read()
    print(readf)
    print("is file closed = ", f.closed)
print("is file closed = ", f.closed)

# absolute path 
with open("D:\Python\Python\demofile.txt","r") as df:
    readd = df.read()
    print(readd)