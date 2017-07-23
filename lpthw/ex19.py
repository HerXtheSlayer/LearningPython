# define function with 2 variables as arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# print out a line which uses 1 variable
    print "You have %d cheeses!" % cheese_count
# print out a line which uses 2nd variable
    print "You have %d boxes of crackers!" % boxes_of_crackers
# print out the sentences
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


# call function with numbers as args
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# set variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# call function with previously set variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# call function with math results as args
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# call function with variable and math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
