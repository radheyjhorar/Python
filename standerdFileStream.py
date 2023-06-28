# Stander File Stream
import sys
print(sys.version)

# 1. sys.sdtin
# 2. sys.sdtout
# 3. sys.sdt

f = open("demofile.txt", "r")

l1 = f.readline()
l2 = f.readline()
l3 = f.readline()
f.close()


with open("demofile.txt", "a") as f:
    sys.stdout.write(l1)    # Direct hardware to software connection
    sys.stdout.write(l2)    # Direct hardware to software connection
    sys.stdout.write(l3)    # Direct hardware to software connection