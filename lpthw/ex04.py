# define cars variable
cars = 100
# define space_in_a_car variable
space_in_a_car = 4
# define drivers variable
drivers = 30
# define passengers variable
passengers = 90
# define cars_not_driven variable
cars_not_driven = cars - drivers
# define cars_driven variable
cars_driven = drivers
# define carpool_capacity variable
carpool_capacity = cars_driven * space_in_a_car
# define average_passengers_per_car variable
average_passengers_per_car = passengers / cars_driven


# print number of available cars (from variable)
print "There are", cars, "cars available."
# print number of available drivers
print "There are only", drivers, "drivers available."
# print how many cars will not be driven
print "There will be", cars_not_driven, "empty cars today."
# print how many people can be transported
print "We can transport", carpool_capacity, "people today."
# print number of passengers
print "We have", passengers, "to carpool today."
# print how many passengers need to go in each car
print "We need to put about", average_passengers_per_car, "in each car."
