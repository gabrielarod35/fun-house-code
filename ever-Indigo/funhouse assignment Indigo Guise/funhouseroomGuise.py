from random import randint
from time import sleep

def roomIndigo(name):
    
    print("Welcome to my room, "+name+"!\n")
    print("This room has two doors, each guarded by a non-descript person.")
    print("One door will reward you with points...the other is a terrible trap.")
    print("One person MUST always lie; the other MUST always tell the truth.")
    print("You may ask ONE of them ONE question.\n")
    input("(Press Enter to continue)")

    ### setting up liar
    liar = randint(1,2)
    if liar == 1:
        liar = "left"
    else:
        liar = "right"

    invalid = 0 #used to punish bad direction following skills for the following inputs.

    ### asking questions...
    askingWho = ""
    lor, bad = inputIntPrompt("longstring1.txt", 2)
    invalid = invalid+bad
    if lor == 1:
        if liar == 1:
            askingWho = "Knave"
        else:
            askingWho = "Knight"
    else:
        if liar == 2:
            askingWho = "Knave"
        else:
            askingWho = "Knight"
    ### askingWho established as string Knight or Knave
    

    question, bad = inputIntPrompt("longstring2.txt", 8)
    invalid = invalid+bad

    response = ""
    ### answering the user's question (several answers are the same for both Knight and Knave)
    if question == 1:
        response = "\n\"My door will reward you for crossing through it!\"\n"
    elif question == 2:
        response = "\n\"Yes, most assuredly.\"\n"
    elif question == 4:
        response = "\n\"My friend's door does.\"\n"
    elif question == 5:
        response = "\n\"A wealth of points awaits behind my door!\"\n"
    elif question == 7:
        response = "\n\"Of course I would!\"\n"
    elif question == 8:
        response = "\n\"A deadly trap awaits you there.\"\n"
    ### \/ the only good questions \/
    elif question == 3:
        if askingWho == "Knave":
            response = "\n\"No, they wouldn't. I'm positive.\"\n"
        else: #askingWho == "Knight"
            response = "\n\"They would, absolutely.\"\n"
    else: #question == 6
        if askingWho == "Knave":
            response = "\n\"Of course they would!\"\n"
        else: #askingWho == "Knight"
            response = "\n\"Of course they wouldn't!\"\n"

    respond = input(response+"\n(Press Enter to continue)")
    ###


    ### making a decision...
    pts = 0
    closure = 0 # checks to see if the player chickened out

    while closure == 0:
        decision, bad = inputIntPrompt("longstring3.txt", 3)
        invalid = invalid+bad
        if decision == 1:
            pts = pts+finalDecision("left", liar) #liar was set WAY at the begining
            closure += 1
        elif decision == 2:
            pts = pts+finalDecision("right", liar)
            closure += 1
        else: #decision == 3
            print("\nSometimes the wisest decision is to cut your losses.")
            print("If you leave now, you won't gain any points from this room...")
            lastchance, bad = inputIntPrompt("longstring4.txt", 2)
            invalid = invalid+bad

            if lastchance == 1:
                print("\nFair enough!\n")
                print("You walk out of the room, earning nothing but also losing nothing.")
                print("However, when you step out of the room...")
                print("You find yourself in a hallway you haven't been before...how mysterious!")
                pts = 0
                closure += 1
            else: #lastchance == 2 (no)
                print("\nThat's the spirit!")

    input("(Press Enter to continue)")

    if invalid > 0:
        print("\n--before you leave, though, there's one last thing...")
        sleep(3)
        print("You've lost", invalid*10, "points for poor direction following. ;)")
        print("Invalid responses have a consequence, you know! It's nothing personal.")
        sleep(3)

    print("\nBye,",name+"! Have fun in the next room!")
    
    finalPoints = pts-(invalid*10)
    return finalPoints
# end roomIndigo()


# # # other functions # # # # # # # # # # # # # # # #

def inputIntPrompt(infile, numOptions):

    valid = 0 #keeps the code looping until a valid answer is given
    bad = 0   #punishes bad responses later
    File = open(infile, "r")
    Text = File.read()

    while valid == 0:
        try:
            choice = int(input(Text))
        except ValueError: #try/except so that the user HAS to enter an int
            print("\nPlease enter a number.")
            bad += 1
        else:
            if 0 < choice <= numOptions:
                valid += 1
            else:
                print("\nPlease choose a valid option.")
                bad += 1
    File.close()
    return choice, bad

def finalDecision(directionStr, liar):
    print("\nYou enter through the", directionStr, "door...\n\n")
    sleep(3)
    print("...\n\n")
    sleep(3)

    pts = 0    
    if directionStr == liar:
        pts = pts+losertext()
    else: #player chose correct path
        pts = pts+winnertext()
    return pts

def losertext():
    print("As you step through...your foot greets nothing but air.")
    print("You tumble into a pit, losing 50 points along the way!")
    print("Don't worry, I'm sure there's a cushion down there to catch you...")
    pts = -50
    return pts

def winnertext():
    print("As you step through...a loud pop goes off above your head.")
    print("Confetti falls from the ceiling as you walk triumphantly through!")
    print("Congragulations, you've earned 50 points! You must be so clever! :)")
    pts = 50
    return pts
