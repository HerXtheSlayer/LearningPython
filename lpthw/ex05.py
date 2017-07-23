name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
height_m = height * 2.5 # cm
weight = 180 # lbs
weight_m = weight * 0.45359237 # kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not to heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricy, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

# convert to metric system
print "He's %d centimeters tall." % height_m
print "He's %d kilograms heavy." % weight_m
