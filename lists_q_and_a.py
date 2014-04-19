def art_project():
    print "The class has met, you have said a prayer, and things are going well. Now it is time for an art project. What sort of project do you do?"
    projects = ["1. Make a skit re-enacting the story we just read.","2. Paint ourselves.","Build houses our of popsicle sticks with virtues on them. Truthfulness is the foundation...","4. Leave it up to the assistant teacher."]
    replys =["11","22","33","44"]
    for choices in projects:
        print choices
    choice = int(raw_input("> "))
    choice -= 1
    print replys[choice]
    pass

art_project()
