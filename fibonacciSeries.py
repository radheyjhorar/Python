def feb(value):
    a, b = 0, 1
    while a < value:
        print(a, end = ' ')
        a, b = b, a+b
    #print()
    
def feb1(value):
    result = []
    a, b = 0, 1
    while a < value:
        result.append(a)
        a, b = b , a+b
    return result


print(feb(1000))
print()
print(feb1(1000))