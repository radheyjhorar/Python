# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

    # {
        # key : "value",
        # key : "value"
    # }

a = { "Name" : "Radhey",
     "Subject" : "English",
     "Marks" : "80"
     }
print(a["Subject"])

for i,j in a:
    print(i, j)
    
a["Subject"] = "Math"
print(a)