def qanda():
    print "How old are you?"
    ques = ["1. 26", "2. ninety", "3. I don't know."]
    ans = ["Pretty young!", "Old man...", "That,s kinda weird."]
    for options in ques:
        print options
    repl = int(raw_input("> "))
    repl -= 1
    print "You said: %r" % ques[repl]
    print ans[repl]

qanda()
