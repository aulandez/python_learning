# Defines the number of cars 
cars = 100
# How many seats each car has
space_in_a_car = 4.0
# How many drivers are available
drivers = 30
# How many people need rides
passengers = 90
# The amount of cars that remain when you subtract the number of drivers from the number of avaialable cars
cars_not_driven = cars - drivers
# The number of cars to be driven is the same as the number of drivers
cars_driven = drivers
# The total number of seats available
carpool_capacity = cars_driven * space_in_a_car
# How many passengers each car will need accounting for the number passengers totoal and cars.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers,  "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print	"We can transport", carpool_capacity, "people today."
print	"We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."