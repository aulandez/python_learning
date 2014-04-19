from sys import argv

script, filename = argv

print "Opening your file, entitled: %r" % filename
print "..."
print "Taking some time..."
print "..."
print "Here it is, sorry for the wait:"

target = open(filename, 'r')

print target.read()