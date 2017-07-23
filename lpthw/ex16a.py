from sys import argv

script, filename = argv

f1 = open(filename)

print "Content of %r:" % filename
print f1.read()
