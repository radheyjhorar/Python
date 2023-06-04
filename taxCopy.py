salary = float(input("Your Salary: "))
saving = float(input("Your Saving: "))
savetax = 0
tax = 0
if saving > 150000:
    savetax = 150000
else:
    savetax = salary
if salary <= 250000:
    tax = 0
elif salary <= 500000:
    tax = (salary - savetax) * 5 / 100
elif salary <= 1000000:
    tax = (salary - savetax) * 20 / 100
elif salary > 1000000:
    tax = (salary - savetax) * 30 / 100
else:
    print("You put some wrong value")

print("Total Salary = ",salary)
print("Save Tax = ",savetax)
print("Tax = ",tax)
print("Salary after Tax = ",salary - tax)
