totalIncome = int(input("Your Income: "))
saving = int(input("Your saving: "))
taxIncome = totalIncome - saving
taxIn = totalIncome - 150

if saving <= 150:
    if taxIncome < 250:
        print("NoTax Income = ",totalIncome)
    elif taxIncome > 250 and taxIncome < 500:
        print("Tax = 5% Salry =",totalIncome - taxIncome * 5 / 100)
    elif taxIncome > 500 and taxIncome < 1000:
        print("Tax = 20% Salry =",totalIncome - taxIncome * 20 / 100)
    elif taxIncome > 1000:
        print("Tax = 30% Salry =",totalIncome - taxIncome * 30 / 100)
    else:
        print("Salary value does not correct")
        
elif saving > 150:
    if taxIncome < 250:
        print("NoTax Income = ",totalIncome)
    elif taxIn > 250 and taxIn < 500:
        print("Tax = 5% Salry =",totalIncome - taxIn * 5 / 100)
    elif taxIn > 500 and taxIn < 1000:
        print("Tax = 20% Salry =",totalIncome - taxIn * 20 / 100)
    elif taxIn > 1000:
        print("Tax = 30% Salry =",totalIncome - taxIn * 30 / 100)
    else:
        print("Salary value does not correct")
else:
    print("Value is not correct")
    

