# Currently contains rooms from Carla and Indigo

def main():

  # get name
  name = input("What is your hero's name? ")

  # initialize points
  points = 0

  print("You are entering the fun house!")

  # 0th room
  dp = roomIndigo(name)
  points = points + dp

  # delay --- Add code to make transition from room to room less abrupt

  # first room
  dp = carlasroom(name)  # dp is the number of points to add or subtract from the point total
  points = points + dp

  





  print("End of the house.  You have ", points," points")



#funhouse homwork game
def carlasroom(name):
    pts = 0
    print("Welcome to my room of the fun house dear", name)
    print("In order to make it out you need 20 star points to exist!")
    print("No more fooling around with introductions now lets start the fun!")
    print()
    print()
    print("How about we start with something simple!")
    print("In front of you are two different pieces of candy. Which do you choose to eat?")
    
    print("The candies in front of you are star shaped and oxegon shaped")
    print("A. Star")
    print("B. Oxegon")
    print()
    answer = input("Which do you choose?  ")     
    if answer == "A":
        print()
        print("Good choice. You have choosen the star candy so now you have gained 5 star points")
        pts = 5 + pts
        pts = pts + ChoiceA(name)
        #return pts
    else:
        print()
        print("You have choosen oxegon shaped candy. unfortunaly for you it was bitter so negative 2 points")
        pts = -2 + pts
        pts = pts + ChoiceB(name)
        #return pts

    return pts

    
# if they choose choice a and color light switches
def ChoiceA(name):
    pts = 0
    print()
    print("Hopfully that star candy was good! Now it is time to go to the next room!")
    print("You walked along the dark hallway to see three individual light switches.")
    print("A.) Red")
    print("B.) Blue")
    print("C.) Yellow")
    print()
    answer = input("Which do you choose? ")
    if answer =="A":
        print()
        print("The red switch has been flipped. The room is filled with a soft red glow.")
        print("you have lost only 3 star points.")
        pts = pts - 3
        pts = pts + Secondroom(name)
        return pts
    elif answer =="B":
        print()
        print("The blue switch has been flipped. The room is filled with a soft blue glow.")
        print("You have gained 5 star points.")
        pts = pts +  5
        pts = pts + Secondroom(name)
        return pts
        
    else:
        print()
        print("Looks like the yellow switch has been turned on. It fills the room with a warm yellow glow.")
        print("You have gained 10 star points.")
        pts = 10  + pts
        pts = pts + Secondroom(name)
        return pts
        
# if they choose choice b and color light switches
def ChoiceB(name):
    pts = 0
    print()
    print("Hopfully that oxegon candy was worth it. Now it is time to go to the next room!")
    print("You walked along the dark hallway to see three individual light switches.")
    print()
    print("A.) Red")
    print("B.) Blue")
    print("C.) Yellow")
    answer = input("Which will you choose?  ")
    if answer =="A":
        print()
        print("The red switch has been flipped. The room is filled with a soft red glow.")
        print("To me dear ",name+" it doesn't look like a good color for the room.")
        print("You have lost only 3 star points.")
        pts = pts -3
        pts = pts + Secondroom(name)
        return pts
    elif answer =="B":
        print()
        print("The blue switch has been flipped. The room is filled with a soft blue glow.")
        print("You have gained 5 star points.")
        pts = 5 + pts
        pts = pts + Secondroom(name)
        return pts
    else:
        print()
        print("Looks like the Yellow switch has been turned on. It fills the room with a warm yello glow.")
        print("You have gained 10 star points.")
        pts = 10 + pts
        pts = pts + Secondroom(name)
        return pts    
#for the second room of the game/ white or black door option
def Secondroom(name):
    pts = 0
    print()
    print("As the room is filled with light you see two different doors ")
    print("Which do you choose to enter? You're half way there my dear",name+".")
    print()
    print("A.) The White Door")
    print("B.) The Black Door")
    print()
    answer = input("Which door do you choose to open?  ")
    if answer ==("A"):
        print()
        print("You open the door to see that there is a room that is pitch black")
        print("All you see above you are a ceiling of glowing specks.")
        print("You have gained 15 star points.")
        pts = pts + 15
        pts = pts + SecondroomA(name)
        return pts
    else:
        print()
        print("It seems like the black door was already chosen.")
        print("You take a peak inside the room to see that it is filled with different colored lights.")
        print("You have gained 5 star points")
        pts = 5 + pts
        pts = pts + SecondroomB(name)
        return pts
 # choice A for the second room/ dark room or black door       
def SecondroomA(name):
    pts = 0
    print()
    print("Do you choose to walk through the dark room dear",name+"?")
    print("A.)Enter into the dark room.")
    print("B.)Choose the black door instead.")
    print()
    answer = input("Its your choise to enter.  ")
    if answer =="A":
        print()
        print("You enter the room and the door slams close behind you.")
        print("You walk around the room with the lights shinning above you until you stumble on a small box")
        pts = pts + box(name)
        return pts
    else:
        print()
        print("Looks like you back tracked and wanted to do to the other door.")
        print("Because you back tracked ",name+" you have lost 2 star points.")
        pts = pts -2
        pts = pts + SecondroomB(name)
        return pts
#choice b for the second room/ you choose black door
def SecondroomB(name):
    pts = 0
    print()
    print("As you enter the room with different colored lights the door slams shut right behind you.")
    print("You walk around the room filled with light until you see a small white box right in front of you.")
    pts = pts + box(name)
    return pts
            
# box Q       
def box(name):
    pts = 0
    print()
    print("Will you open the box?")
    print("A.) Yes")
    print("B.) No")
    print()
    answer = input("Seems rather tempting to open it doesn't it.  ")
    if answer == "B":
        print()
        print("Good choice it was locked. Plus 5 star points.")
        print("You keep the box closed for now and head on your way")
        pts = 5 + pts
        pts = pts + Thirdroom(name)
        return pts
    else:
        print()
        print("You reached already start to open the box only to find it lock.")
        print("You lost 2 star points.")
        print("Looks like you have to find a key now",name+". I have a feeling there is going to be a key in the next room.")
        pts = -2 + pts
        pts = pts + Thirdroom(name)
        return pts
        
#thrid room of fun house
def Thirdroom(name):
    pts = 0
    print()
    print("After exiting the room you where just in you found a area in which is has vases filled with flowers.")
    print("Which flowers for the vases do you pick up",name+"?  ")
    print("A.) The vase filled with Roses")
    print("B.) The vase filled with Sunflowers")
    print()
    answer = input("They both look pretty to pick. Hopefully you don't break the vase.  ")
    if answer == "A":
        print()
        print("When you pull out a single rose you accidentally take the vase with you.")
        print("There is now broken shards of glass but at least you found a key among the broken vase and scattered roses.")
        print("you have lost 5 star points due to the vase being broken. Sorry about that",name+".")
        print("It was a mistake to have the flower vases on the endge of the table.")
        pts = -5 + pts
        pts = pts + Boxq(name)
        return pts
    else:
        print()
        print("You choose the vase filled with Sunflowers. As you take out one of the sunflowers you seemto take the vase with you.")
        print("There is now broken shards of glass but at least you found a key among the scattered sunflowers.")
        print("you have lost 2 star points due to the vase being broken. Sorry about that",name+".")
        print("It was a mistake to have the sunflower vase on the endge of the table.")
        pts = -2 + pts
        pts = pts + Boxq(name)
        return pts
#box Q once again
def Boxq(name):
    pts = 0
    print()
    print("You walk by the broken vase pieces and scattered flowers to go to the last room.")
    print("At least no one got hurt! ")
    print("Now that you have a key do you want to open the box? ")
    print()
    print("Will you open the box?")
    print("A.) Yes")
    print("B.) No")
    print()
    answer = input("Seems rather tempting once again to open it doesn't it.  ")
    if answer == "A":
        print()
        print("You try to open the box with the key you have gotten but it seems like it doesn't fit!")
        print("Looks like that isn't the key you need",name+" but it didn't hurt to try! You get at least 2 star points for trying it.")
        pts = -2 + pts
        pts = pts + Finalroom(name)
        return pts
    else:
        print()
        print("Good choice once again",name+".")
        print("You see that the key is too big for the box itself you save it for the last room up ahead")
        print("You get 2 points for not trying the key.")
        pts = 2 + pts
        pts = pts + Finalroom(name)
        return pts
#final room of fun house   
def Finalroom(name):
    pts = 0
    print("Looks like this is the last room to gain points so lets continue.")
    print("You walk into a room filled with with different constellations to see two doors that lead to the exit.")
    print("Which door do you choose?")
    print("A.) Left")
    print("B.) Right")
    print()
    answer = input("Final door to choose!")
    if answer == "A":
        print()
        print("You walk to the left door and see that the key you got from the broken vase opens the door.")
        print("When you walk out of the room to see the exit sign of the fun house you see a small key by the hallway.")
        pts = pts + Boxq2(name)
        return pts

    else:
        print()
        print("The right door is already in vies as you walk towards it.")
        print("WHen you walk out of the room to see the exit sign of the fun house and a small key by the hallway")
        pts = pts + Boxq2(name)
        return pts

# box Q again
def Boxq2(name):
    pts = 0
    print("For one last chance at using that key do you finally open that box you got from a few rooms back?")
    print("So,",name+"will you open the box?")
    print("A.) Yes")
    print("B.) No")
    print()
    answer = input("Now or never")
    if answer == "A":
        print()
        print("As you open the box you have gained 10 star peices.")
        print("Good things come from those who wait.")
        pts = 10 + pts
        pts = pts + Goodbye(name)
        return pts
    else:
        print()
        print("You take one last look at the box and decide to throw it in the trash.")
        print("The box is gone now as well as the key ")
        print("Who knows what was in the box anyway.")
        pts = pts + Goodbye(name)
        return pts
#The final goodbye
def Goodbye(name):
    pts = 0
    print()
    print("Thanks for playing my room in the fun house!")
    print("Hopefully you try the other rooms in the game",name+"!")
    return pts







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


# gaby's room 
def main(): 
  name = input("What is your hero's name?")
  
  points = 0 
  
  dp  = Gaby's game 
  points = points + dp 
  print("Welcome ,"name+"!")
  print("Your adventure begins")
  print("There are 2 cups n the table, one blue and one red")
  print("Be careful, a spider lives in one of them that will take you back to your previous roound -40 point")
  print("The other cup has a code to advabce to the nect round")
  input("Which cup do you choose? red or blue")
  answer = input("Which cup do you choose? red or blue")
  if answer == "red"
    print("Better luck next time, -40 points")
    points = -40 
  if answer == "blue"
    print("CONGRATS! You have discovered the code, +50 points")
    points = +60
    print("Advance to the next level")
    return points 


#eric's room
Def main():
  name = input("What is your heros name?")
  points = 0
  
  dp = Eric`s room(name)
  points = points + dp
  print("good to have you in this game, ",name+"!")
  print(" Let the game begin!!")
  print("there are two buttons in this room one is red the other is blue")
  print("watch out for the red button it can send you back to the previous room by -25 points")
  print(" the blue button can instantly send you to the final stage of this game by +50 points")
  input("which button do you press? red or blue")
  if answer == "red":
    print("unlucky, go back to the previous room, -25")
    points = -25
  if answer == "blue":
    print(" great job dude, +50)
    points = +50
    print(" goodluck in your future endevors")
    return points
