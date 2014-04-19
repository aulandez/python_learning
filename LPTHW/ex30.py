#!/usr/bin/python
# -*- coding: utf-8 -*-
# Sets values for the variables 'people', 'cars', and 'buses'

people = 67
cars = 6
buses = 44

# If there are more cars than people, print the line

if cars > people:
    print 'We should take the cars.'
elif cars < people:

# If the if aove doesn't work, check if there are more people than cars, and print the line

    print 'We should not take the cars.'
else:

# if neither if above is true, print the line

    print "We can't decide."

# If there are more buses than cars, print the line

if buses > cars:
    print "That's too many buses."
elif buses < cars:

# If the above is false, and there are more cars than people, print the line

    print 'Maybe we could take the buses.'
else:

# If the 'if' and the 'elif'  don't work, print the line

    print "We still can't decide."

# if there are more people than buses print the line

if people > buses:
    print "Alright, let's just take the buses."
else:

# otherwise, print this line (If people are equal to or less than buses.)

    print 'Fine, lets stay home then.'

if cars + buses > people:
    print 'Thats a great number of vehicles.'
else:
    print 'What a crowd!'
