# Binary File Opration

import pickle   #nimport pickle module

# appending binary file
def appendFile(fName, appendValue):
    with open(fName, "ab") as f:       # ab means append binary. f is a var name
        pickle.dump(appendValue, f)
# with-open no need to close file
fileName = "test.dat"
list1 = [10, 20, 30, 40, 50, 60]
appendFile(fileName, list1)        


# Read binary file
with open("test.dat", "rb") as f:  
    l1 = pickle.load(f)
    print(l1)
    
    
# open a jpg in binary mode
# with open("F:\myimage\myImage.jpg", "rb") as imagef:
#     content = imagef.read()
#     print(content)

# with open("test.txt", "ab+") as fileObj:
    
#     print('Input roll and name 5 students\n')
#     for i in range(5):
#         roll = int(input("Roll: "))
#         name = input("Name: ")
#         data = {roll, name}
        
#         pickle.dump(data, fileObj)
        
# print("All data stored successfully")

with open("test.txt", "rb") as fileObj:
    for i in range(14):
        f = pickle.load(fileObj)
        print(f)


    
# f=open("binfile.bin","wb")
# num=[5, 10, 15, 20, 25]
# arr=bytearray(num)
# f.write(arr)
# f.close()

# f=open("binfile.bin","rb")
# rf = f.read()
# print(rf)
# f.close()