from graphics import *

# Fun House Game Homework

# initial points
ptshistory = [0]

def initialpts():
    return ptshistory[0]
def gamepts():
    return ptshistory[-1]
# how the points will be added up during the game
def ptsaffects(delta):
    ptshistory.append(gamepts() + delta)
    return gamepts()




# <<<THE GAME BEGINS HERE>>>



def torrgame(name):
    print("Welcome to my room in the fun house,",name+"!")
    print("Let's get started.\n")

    print("You wake up in a room dark room with a lighter, a hammer, and a key.")
    print("Your goal is to make it out of this room alive...\n")

    print("You have a few options,",name+".")
    print("A: Use the hammer on the door.")
    print("B: Use the lighter.")
    print("C: Throw the key.\n")
    answer = input("What do you decide to do next?\n")

    if answer == "B":
        print("You light up the lighter and notice a fire place. You walk over and start the fire which lights up the room.")
        print("Points =",ptsaffects(5))
        choseB()
    elif answer == "A":
        print("You swing and miss ending up hurting your leg...")
        print("Points =",ptsaffects(-3))
        choseA()
    elif answer == "C":
        print("You throw the key on the ground. You will need the key later...")
        print("Points =",ptsaffects(-1))
        choseC()
    else:
        print("Try again")


        
# after choosing answer "A"
def choseB():
    print("You see the door in front of you. It is barricaded with wood.\n")

    print("Your options are:")
    print("D: Use the hammer to remove the wood.")
    print("E: Light the wood on fire.")
    print("F: Try to jam the key into the keyhole of the door.\n")
    answer = input("What do you plan on doing?\n")

    if answer == "D":
        print("You have successfully removed the wood from the door.")
        print("Points =",ptsaffects(5))
        choseD()
    elif answer == "E":
        print("You end up catching the house on fire...")
        choseE()
    elif answer == "F":
        print("You end up snapping your key in half because the wood was still in the way.")
        print("Points =",ptsaffects(-3))
        chose(F)
    else:
        print("Try again")

        

# after choosing answer "D"
def choseD():
    print("You try to open the door, but it is locked.\n")

    print("Your options are:")
    print("G: Use the hammer to break the lock.")
    print("H: Use the key to open the lock.\n")
    answer = input("What is your next move?\n")

    if answer == "G":
        print("You have succesfully opened the door and gotten out, however, you ended up hurting yourself in the process.")
        print("You have won the game\n")
        print("CONGRATULATIONS\n")
        print("Final points =",ptsaffects(-2))
    elif answer == "H":
        print("You unlock the door and step outside.\n")
        print("You win the game\n")
        print("CONGRATULATIONS\n")
        print("Final points =",ptsaffects(10))
    else:
        print("Try again")




# after choosing A
def choseA():
    print("You still can't see what is in front of you...\n")

    print("Options remain the same:")
    print("B: Use the lighter.")
    print("C: Throw the key.\n")
    answer = input("What do you decide on doing?\n")

    if answer == "B":
        print("You light up the lighter and notice a fire place. You walk over and start the fire which lights up the room.")
        print("Points =",ptsaffects(5))
        choseB()
    elif answer == "C":
        print("You throw the key on the ground. You will need the key later...")
        print("Points =",ptsaffects(-1))
        choseC()
    else:
        print("Try again")


# after choosing C
def choseC():
    print("You pick up the key you threw and notice a fire place.\n")
    print("B: Use the lighter.\n")
    answer = input("You only have 1 option...\n")

    if answer == "B":
        print("You light up the lighter and notice a fire place. You walk over and start the fire which lights up the room.")
        print("Points =",ptsaffects(5))
        choseB()
    else:
        print("Try again")


# after choosing E
def choseE():
    print("Because of this, you are trapped inside...\n")
    print("You lose the game\n")
    print("GAME OVER")




# after choosing F
def choseF():
    print("The door is still in front of you and it is still barricated with wood...\n")
    print("Your options still remain the same:")
    print("D: Use the hammer to remove the wood.")
    print("E: Light the wood on fire.")
    answer = input("What do you decide on doing?\n")
    if answer == "D":
        print("You have successfully removed the wood from the door.")
        print("Points =",ptsaffects(5))
        choseD()
    elif answer == "E":
        print("You end up catching the house on fire...")
        choseE()
    else:
        print("Try again")
