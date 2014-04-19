# i = 0
# numbers = []

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i


# print "The numbers: "

# for num in numbers:
#     print num

def drill_1(n,l):
    i = 0
    numbers1 = []
    while i < n:
        print "\nAt the top of the function 'i' is %d" % i
        numbers1.append(i)
        i = i + l
    print numbers1

print "\nRunning function with value of three 3 and and increment of 1:"
drill_1(3,1)      

print "\nNow we are setting out own value."
drill_1(int(raw_input("\nWhat value do you want? \n> ")),
        int(raw_input("\nAnd that increment? \n> ")))

def drill_2(s,e,c):
    i = 0
    numbers2 = []
    for i in range(s,e,c):
        print "\nAt the top of the loop 'i' is %d" % i
        numbers2.append(i)
    print numbers2   

print "\nNow running as a loop with arbitary values"
drill_2(1,6,1)    

print "\nNow setting our own value in the loop"
drill_2(int(raw_input("Starting value:\n> ")), int(raw_input("End value:\n> ")), int(raw_input("Increment:\n> ")))

