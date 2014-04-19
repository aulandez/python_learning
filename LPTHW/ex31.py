print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input(">")

if door == "1":
    print "There's a giant bear here eating cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."
    print "3. Give the bear a hug."

    bear = raw_input(">")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    elif bear == "3":
        print   "Weird decision. The bear doesn't appreciate your hug and walks out the door. You survive. What do you do now?"
        print "1. Head home?"
        print "2. Eat the rest of the bear's cake?"
        print "3. Follow the bear."
        hug = raw_input(">")

        if hug == "1":
            print "You walk home, it takes you six hours. The sun sets and in the dark you trip over a tree root and fall on a bear trap. Your skull is crushed and mascerated. Good job!"
        if hug == "2":
            print "The cake was made of almond flour and cyanide. You vomit yourself to death. Good job!"
        if hug == "3": 
            print "The bear is really fast" # Expand here.
            print "1. Run really fast to catch up."
            print "2. Try to jump on to the bear's back."
            print "3. Skateboard after the bear."
            print "4. Throw a rock at the bear's head."
            print "5. Give up"
            fast = raw_input(">")
            if fast == "1" or fast == "2":
                print "The bear doesn't notice you. The two of your end up at a cave under a waterfall. The bear walks deeper into the cave. You fall behind, what do you do?"
            elif fast == "3":
                print "You can't skateboard in a forest dumbass. You try, fall and die. Good job!"
            elif fast == "4":
                print "You miss. The bear notices, and claws your eyes out. Good job!"
            else:
                print "You are a wimp. You die."
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else: 
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good Job!"
