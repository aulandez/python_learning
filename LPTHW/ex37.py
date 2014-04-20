# and: boolean operator, returns false if false is present
print True and False

# del: deletes an item from a list using it's index
list1 = [1,2,3,4]
print list1
del list1[0]
print list1

# from: specifies which module to import an object from
from sys import exit
# not: reverses the truth of any boolean expression
print not(True and True)
# while: loops through the code as long as a condition is true
hi = 1
while hi < 5:
    print "hi = %r" % hi
    hi += 1

# as: rename imported object

# elif: runs a piece of code when preceding if or elif was false
if hi == 4:
    print "if"
elif hi == 5:
    print "elif"
else:
    print "else"

# global: allows a variable that is defined and altered in one function to be used and altered in another
# or: boolean operator, returns true as long as one true is present
print True or False

# with: I DON'T UNDERSTAND THIS ONE YET

# assert: causes error if condition is false
assert True

# else: ends a string of if elifs, can be used cover unspecified things
# if: runs a bit of code if a condition is true
if 1 == 1:
    print "Obviously!"
else:
    print "Weird..."

# pass: null operation, usefull as a placeholder
def function1():
    pass
function1()
# yield
# break: terminates the current loop and resumes execution at the next statment
for letter in "example":
    if letter == 'p':
        break
    print "Current Letter: ", letter
print "BROKEN"
# except
# import: imports an object from another module
""" from module import example
    import module.example    """
# print: returns thetext enclosed in ""
print "Printing is so fun"
# class
# exec
# in
# raise
# continue
# finally
# is
# return
# def
# for
# lambda
# try
# True
print "Some True things:"
print "1 + 1 = 2"
print "\t", 1 + 1 == 2
print "True or False"
print "\t", True or False

# False
print "Some False things:"
print "1 + 36 = 2"
print "\t", 1 + 36 == 2
print "True and False"
print "\t", True and False

# None
# strings
print "Strings:"
print "\"This is a string\""
print "So is this: \'2567693344343\'"

# numbers
print """These are numbers:
2
3
4
67
34"""

# floats
print """These are floats:
2.5
3.0
5.445
3.0
0.0
0.4"""

# lists
print "Lists look like this:"
print "list1=[1,2,3,4,5]"
print "list2=[\"string1\", \"string2\", \"string57\"]"
print 'Just remember, items in lists are accessed using their index, not their ordinal number! This is critical.'
# \\
# \'
# \"
# \a
# \b
# \f
# \n
# \r
# \t
# \v
# %d
# %i
# %o
# %u
# %x
# %X
# %e
# %E
# %f
# %F
# %g
# %G
# %c
# %r
# %s
# %%
# +
# -
# *
# **
# /
# //
# %
# <
# >
# <=
# >=
# ==
# !=
# <>
# ( )
# [ ]
# { }
# @
# ,
# :
# .
# =
# ;
# +=
# -=
# *=
# /=
# //=
# %=
# **=
