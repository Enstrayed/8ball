import random

exit = False
affirm1 = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it."]
affirm2 = ["As I see it, yes.", "Most likely.", "Outlook Good.", "Yes.", "Signs point to yes."]
noncommit = ["Reply hazy, try again.", "Ask again later.", "Better not tell you know.", "Cannot predict now.", "Concentrate and ask again."]
negative = ["Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
pool = [affirm1, affirm2, noncommit, negative]

while exit == False:
    if input() != "exit":
        print(pool[random.randrange(0,4)][random.randrange(0,4)])
    else:
        exit = True
