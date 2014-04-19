# Imports the argv feature from the module sys
from sys import argv

# sets the arguments needed for argv
script, input_file = argv

# defines a function that displays an entire text. "f" is just a variable
# name for the file. 'print_all' just requires that one argument/variable
def print_all(f):
    print f.read()

# the 'rewind' function seeks the 0th byte of whatever file is fed in as f
def rewind(f):
    f.seek(0)

# this function prints the line number and the contents of the line. The 
# two arguments define the line and the file.
def print_a_line(line_count, f):
    print line_count, f.readline()

#creates a variable of the 'input_file' argument
current_file = open(input_file)

print "First let's print the whole file:\n"

# runs the 'print_all' function on the 'current_file' variable
print_all(current_file)

print "Now let's rewind, kind of like a tape"

# runs the 'rewind' function on the 'current_file' variable
rewind(current_file)

print "Let's print three lines:"

# defines the current_line variable as equal to 1, the first line of the file
current_line = 1
# prints the contents of the first line (current_line = 1)
print_a_line(current_line, current_file)

# increments the current_line variable 
current_line =+ 1
# prints the contents of the second line (current_line = 2)
print_a_line(current_line, current_file)

# same as above
current_line =+ 1
#  (current_line = 3)
print_a_line(current_line, current_file)

# current_line becomes line_count because it is used where the line_count
# argument is demanded and it's most recently defined value becomes the value of
# the argument line_count