# this imports the "argv" feature from the module "sys" that allows arguments
# to be added to the command line call.
from sys import argv

# this creates the two variables that need to be entered into the command 
# line as arguments when the script is run.
script, filename = argv

# txt is a function that displays what open give back to it ?
txt = open(filename)

#prints the name of the file given as an argument to the command line as well 
#as printing the content of the variable 'filename' given to 'txt'above.
print "Here's your file %r:" % filename
print txt.read()

# makes you put in the filename as raw input.
print "Type the filename again:"
file_again = raw_input("> ")

# Again this fills the variable txt_again with the contents of the file
txt_again = open(file_again)

# prints the contents of the file given to the variable txt_again

print txt_again.read()
txt.close()
txt_again.close()