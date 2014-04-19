# This line sets up a line to print when X is the variable
x = "There are %d types of people." % 10
# the variable binary prints the word binary
binary  = "binary"
# the variable do_not prints the word don't
do_not = "don't"
# variable y print the stence with the variables binary and don't showing their values.
y = "Those who know %s and those who %s." % (binary, do_not)
# prints the two sentences, calling on the three values defined in the variables
print x
print y

#Prints two new sentences that contain the predefined variables as parts of them. Strings made up of other strings.
print "I said %r." % x
print "I also said '%s'." % y

# two variables
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# prints a string composd of the two variables above
print joke_evaluation % hilarious

# defines two printed strings
w = "This is the left side of..."
e = "a string with a right side."

# Uses the variables to create a string composed of two smaller strings.
print w + e