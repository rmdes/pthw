# 24 + 34 * 25 / 100 - 1023

# 

print(24 + (34 * 25 / 100) - 1023)


def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    mult = a * b
    return mult

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


mul =  multiply(34, 24)
div = divide(mul,100)
plus = add(div,24)
sous = substract(plus,1023)

print(sous)
# print(f"Résultat: {sous}")
