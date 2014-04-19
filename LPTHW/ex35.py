from sys import exit

def start():
    print "You are in a dark room.\nThere is a door to your right and left.\nWhich one do you take?"

    next = raw_input("> ")

    if "left" in next:
        bear_room()
    elif "right" in next:
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


def bear_room():
    print "There is a bear here.\nThe bear has a bunch of honey.\nThe fat bear is in front of another door.\nHow are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif "taunt" in next and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif "taunt" in next and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif "open" in next or "door" in next and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def gold_room():
    print "This room is full of gold. How much do you take"

    next = raw_input("> ")
    if int(next) < 50:
        print "Nice, you're not greedy, you win."
        exit(0)
    if int(next) > 50:
        dead("You greedy bastard")
    else:
        dead("Man, learn to type a number.")


def cthulhu_room():
    print "Here you see the great evil Cthulhu.\nHe, it, whatever stares at you and you go insane.\nDo you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "Good job!"
    exit(0)


start()