name = 'Zed A. Shaw'
age = 23 # not a lie
height = 72.0 # inches
weight = 175.0 # lb
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
met_weight = weight *.453592
met_height = height * 2.54

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee" % teeth
print "In europe he weighs %d kilograms, and is %d centimeters tall." % (met_weight, met_height)

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d" % (age, height, weight, age + height + weight)