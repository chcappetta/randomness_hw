import random

def winner():
    winner = random.randint(1,3)
    return(str(winner))
def roll():
    roll = random.randint(1,6)
    choice = (roll%3)+1
    return(str(choice))

thisw = winner()
thisc = roll()

def setblocked(w,c):
    blocked = 0
    if w == c:
        if w == "1":
            blocked = random.randint(2,3)
        elif w == "2":
            num = random.randint(0,1)
            if num == 0:
                blocked = 1
            else:
                blocked = 3
        else:
            blocked = random.randint(1,2)
        return(blocked)
    else:
        if w == "1":
            if c == "2":
                blocked = 3
            elif c == "3":
                blocked = 2
        if w == "2":
            if c == "1":
                blocked = 3
            elif c == "3":
                blocked = 1
        if w == "3":
            if c == "1":
                blocked = 2
            elif c == "2":
                blocked = 1
    return(blocked)

def dogmath(w, c, b):
    print("You chose: " + c)
    print(str(b) + " is not a winner. Switch your choice?")
    newc = (input("your choice [1,2,3]: "))
    return(newc) 

def choose(w, newchoice):
    if newchoice == w:
        print("you win!")
    else:
        print("you lose")
    return

blocked = setblocked(thisw, thisc)
choose(thisw,dogmath(thisw,thisc,blocked))
