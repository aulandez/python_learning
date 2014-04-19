# This line defines the function 'cheese_and_crackers', it contains two
# arguments and prints four lines that use those arguments.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

# This line fills that two arguments of the function with two numbers supplied
# directly
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Names two variables that can be supplied as arguments for the function
print "OR, we can use variables from our script:"
amount_of_cheese   = 10
amount_of_crackers = 50

# Calls the function with the two variables defined above as its arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Calls the function with two math problems supplied to fill the arguments
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Calls the function, supplies two variables as arguments and alters them with
# math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def party_invitees(girls, boys):
    print "We have invited %d girls," % girls
    print "and around %d boys." % boys
    print "Technically they are all men and women"
    print "So there should be %d adults at the party" % (girls + boys)
    print "\n"

#call1
party_invitees(10, 12)

#call2
amount_of_girls = 22
amount_of_boys  = 33
party_invitees(amount_of_girls, amount_of_boys)

#call3
party_invitees(22 - 2, 33 - 5 + 6)

#call4
print "How many girls did you invite again?"
girls_inv = int(raw_input())
print "\nAnd boys? "
boys_inv = int(raw_input())
print "\n"
party_invitees(girls_inv, boys_inv)

#call5
print "Wait, sorry, I forgot how many boys you said, tell me again?"
boys_again = int(raw_input())
print "Okay, so..."
party_invitees(girls_inv, boys_again)

#call6
print "I invited a few more people, 2 extras of each gender, new numbers."
party_invitees(girls_inv + 2, boys_inv +2)

#call7
print "We can pass a function as arguments."
print "We can now ask the user for the number of boys and girls a different way:"
party_invitees(int(raw_input("How many girls?")), int(raw_input("How many boys?")))

#call8
print "We can call a function in  a loop, calling it 10 times:"
for i in range(10):
    party_invitees(20, 30)

#call9
pinv = party_invitees
pinv(41, 2)

#call10
import random
rand1 = random.randrange(1, 10)
rand2 = random.randrange(1, 10)
pinv(rand1, rand2)
