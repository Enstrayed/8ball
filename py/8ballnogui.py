from tkinter import *
from tkinter import ttk
import random
import sys

responsesAffirm1 = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it."]
responsesAffirm2 = ["As I see it, yes.", "Most likely.", "Outlook Good.", "Yes.", "Signs point to yes."]
responsesNonCommit = ["Reply hazy, try again.", "Ask again later.", "Better not tell you know.", "Cannot predict now.", "Concentrate and ask again."]
responsesNegative = ["Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
poolManifest = ["Affirm1","Affirm2","NonCommit","Negative"]

# returns number within range for stored responses
# example: print(responsesAffirm1[getRng("ans")])
# in english: print a random response from the pool using the answer range
def getRng(type):
    switch={
        "typ":random.randrange(0,4),
        "ans":random.randrange(0,5)
    }
    return switch.get(type)

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

def getPool():
    return str_to_class('responses'+poolManifest[getRng("typ")])

# debugging step; print random response 
print(getPool()[getRng("ans")])

# root = Tk()

# frm = ttk.Frame(root, padding=10)
# frm.grid()


# ttk.Label(frm, textvariable=getPool()[getRng("ans")]).grid(column=0, row=0)
# ttk.Button(frm, text="Roll",).grid(column=0, row=1)


# root.mainloop()