# Simple Interest 

# principal = 10000
# rate = 2
# time = 2
# simpleIntrest = principal * rate * time / 100
# print(simpleIntrest)
# amount = simpleIntrest + principal
# print(amount)


# Simple Interest Amount Change = Rate change

principal = int(input("Please enter Principle:"))
rate = 2
time = int(input("please enter time Year/Month:"))
if principal < 10000:
    rate = 3

if principal > 10000:
    rate = 4

simpleIntrest = principal * rate * time / 100
print(simpleIntrest)
amount = simpleIntrest + principal
print(amount)