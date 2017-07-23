# get argv from sys module
from sys import argv

# get filename as argument for the script
script, filename = argv

# open the filename
txt = open(filename)

# show the text
print "Here's your file %r:" % filename
# show content of the file
print txt.read()

# show txt
print "Type the filename again:"
# ask for the filename
file_again = raw_input("> ")

# open file and put it in variable
txt_again = open(file_again)

# read the file and print it
print txt_again.read()
