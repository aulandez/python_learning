"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
"""

from sys import exit

def start():

    print "What is your name?"
    name = raw_input("> ")
    print "So, %r, you have decided to start a children's class?" % name
    yesno = raw_input("> ")

    if "yes" in yesno or "Yes" in yesno:
        parents()
    else:
        print "Yes or no. "
        crisis("setback")

def parents():

        print "Well then, we should talk with some of the parents of the children you have in mind."
        print "Let's get them together."
        print "..."
        print "The parent's are gathered together, one of them has a question:"
        print "\"So, what are these classes all about?\""
        print "How do you respond?"
        print "1. Well, they are classes where children learn how to become Baha'is."
        print "2. We teach them virtues, and how to be nice."
        print "3. In these classes, the children learn about universal spiritual principles and explore how they are applied through arts, games, prayer, and study of stories and quotations from the Baha'i Faith and other world religions. "

        while True:
            answer = int(raw_input("> "))
            if answer == 1:
                print "The parent's are very offended. They don't want their kids in your class."
                crisis("setback")
            elif answer == 2:
                print "The parents aren't super enthusiastic, but they let their kids come."
                helper()
            elif answer == 3:
                print "The parents are really excited by this answer. They ask a few more questions and agree that the class is a good idea."
                helper()
            else:
                print "Huh?"

def helper():

    print "Now you need a helper!"
    print "Three youth in the neighborhood you live in are ready and able to help teach your class. You need to pick one. Here are your choices."
    print "1. Alex is sixteen. He needs some community service hours, so wants to help out. He came to one session of a study circle but found it pretty boring. He really likes shoes, and texting."
    print "2. Grace is sixteen. She studied Ruhi Books 1 and 3 after "
    helper = int(raw_input("> "))
    if helper == 1:
        print "Good choice..."
    elif helper == 2 or helper == 3:
        print "Good choice!"
    art_project(helper)

def art_project(helper):
    print "The class has met, you have said a prayer, and things are going well. Now it is time for an art project. What sort of project do you do?"
    projects = ["1. Make a skit re-enacting the story we just read.","2. Paint ourselves.","Build houses our of popsicle sticks with virtues on them. Truthfulness is the foundation...","4. Leave it up to the assistant teacher."]
    replys =["The children perform their skits. They are awkward and adorable. They really seem to have learned something.","The children misinterpret your instructions and paing on themselves. The paint is acrylic and doesn't easily wash off. The parents aren't pleased.","Great project idea, The kids love it and their parents think it is great. Whenever you do a home visit now you see their popsicle-houses on the mantle.","The assistant teacher decides the children should do the human knot. It doesn't seem related and they become distracted and frustrated. Half of the parents decide not to send them back."]
    for choices in projects:
        print choices
    choice = int(raw_input("> "))
    choice -= 1
    print replys[choice]
    if choice == 1:
        crisis("setback")
    elif choice == 3 and helper == 1:
        crisis("fail")
    elif choice == 3 and helper == 2:
        crisis("setback")
    elif choice == 0 or choice == 2:
        print "Good job!"
        bad_behavior()

def bad_behavior():
    pass

def progress_report():
    pass

def win():
    pass

def crisis(kind):

    if kind == "setback":
        print "Reflect on your actions and try again."
        start()
    elif kind == "fail":
        print "Wow! That was a serious messup. Maybe you should find a different kind of service."
        exit()
    else:
        exit()

print "\nWelcome to \"Children's Class\" the Game. Now commencing a path of service!"
print "This game was made by Gerald Fernandez-Mayfield in 2014 and is distributed under the terms of the Unlicense <unlicense.org>\n"
start()
