# Binary File Opration

import pickle

list = [10, 20, 30, 40, 50, 60]
with open("test.dat", "ab") as f:
    pickle.dump(list, f)
  
with open("test.dat", "rb") as f:  
    l1 = pickle.load(f)
    print(l1)