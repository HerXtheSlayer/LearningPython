def add(a, b):
    print "Adding %d + %d" % (a,b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b


dafaq = add(24, subtract(divide(34, 100), 1024))

print "and that's: ", dafaq

def mars(a, b):
    return a * b * a / b

voda = mars(36, 29)
print "udaljenost do marsa je: %d" % voda
