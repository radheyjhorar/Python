import os

def creatFile(fileName):
    try:
        with open(fileName, 'w') as f:
            f.write('Hello World!\n')
        print("File " + fileName + " created successfully.")
    except IOError:
        print('Error: could not created file ' + fileName)

def readFile(fileName):
    try:
        with open(fileName, "r") as f:
            content = f.read()
            print(content)
    except IOError:
        print("Error: clould not read file " + fileName)

def appendFile(fileName, text):
    try:
        with open(fileName, "a") as f:
            f.write(text)
        print("Text appended to file " + fileName + " Successfully")
    except IOError:
        print("Error: could not append to file " + fileName)

def renameFile(fileName, newFileName):
    try:
        os.rename(fileName, newFileName)
        print("File " + fileName + " renamed to " + newFileName + " successfully.")
    except IOError:
        print("Error: could not rename file " + fileName)
        
def deleteFile(filename):
    try:
        os.remove(filename)
        print("File " + filename + " deleted successfully!")
    except IOError:
        print("Error: could not deleted file " + filename)
        
print(deleteFile("example"))