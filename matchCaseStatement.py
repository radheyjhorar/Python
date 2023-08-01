# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = ["Rahul", "Radhey", "Ram", "Avinash", "Vabhav", "Kunal", "Rishi", "Kirti", "Elvish"]
# z = int(input("Enter Student's roll no. : "))

# for i in x:
#     match z:
#         case i:
#             print(y[i-1])    
#             break
 
c = int(input("Please enter any number: "))
match c:
    case 786:
        print("Welcome sir, Have a nice day")
    case _ if 100 > c:
        print("The enter number is less then 100")
    case _ if 100 < c and 500 > c:
        print("The enter number is between 100 t0 500")
    case _ if 500 < c and 786 > c:
        print("Your number between 500 to 786")
    case _ if 786 < c:
        print("The entered number is above 786")
    # case _ :
    #     print("Sorry, Your Code is Wrong:", c)
    
        