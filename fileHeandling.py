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
f = open("demofile.txt", "a")
while True:
    str = input("Enter string: ")
    f.write("\n" + str)
    print("for continue press -y- for close press -c-")
    inp = input("Y OR C: ")
    if inp != "y":
        break
f.close()

# AFTER WRITE READ THE FILE
f = open("demofile.txt", "r")
print(f.read())




# FILE APPENDING
# f1 = open("demofile.txt", "a")
# str1 = "Hellow world what's going on \n"
# f1.write(str1)
# f1.close()
# # READ FILE AFTER APPENDING
# f1 = open("demofile.txt", "r")
# print(f1.read())
# f1.close()



