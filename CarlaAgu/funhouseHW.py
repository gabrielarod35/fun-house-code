#funhouse homwork game
def carlasroom(name):
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
        pts = 5
        ChoiceA(name)
        return pts
    else:
        print()
        print("You have choosen oxegon shaped candy. unfortunaly for you it was bitter so negative 2 points")
        pts = -2
        ChoiceB(name)
        return pts
# if they choose choice a and color light switches
def ChoiceA(name):
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
        pts = -3
        Secondroom(name)
        return pts
    elif answer =="B":
        print()
        print("The blue switch has been flipped. The room is filled with a soft blue glow.")
        print("You have gained 5 star points.")
        pts = 5
        Secondroom(name)
        return pts
        
    else:
        print()
        print("Looks like the yellow switch has been turned on. It fills the room with a warm yellow glow.")
        print("You have gained 10 star points.")
        pts = 10
        Secondroom(name)
        return pts
        
# if they choose choice b and color light switches
def ChoiceB(name):
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
        pts = -3
        Secondroom(name)
        return pts
    elif answer =="B":
        print()
        print("The blue switch has been flipped. The room is filled with a soft blue glow.")
        print("You have gained 5 star points.")
        pts = 5
        Secondroom(name)
        return pts
    else:
        print()
        print("Looks like the Yellow switch has been turned on. It fills the room with a warm yello glow.")
        print("You have gained 10 star points.")
        pts = 10
        Secondroom(name)
        return pts    
#for the second room of the game/ white or black door option
def Secondroom(name):
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
        pts = 15
        SecondroomA(name)
        return pts
    else:
        print()
        print("It seems like the black door was already chosen.")
        print("You take a peak inside the room to see that it is filled with different colored lights.")
        print("You have gained 5 star points")
        pts = 5
        SecondroomB(name)
        return pts
 # choice A for the second room/ dark room or black door       
def SecondroomA(name):
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
        box(name)
    else:
        print()
        print("Looks like you back tracked and wanted to do to the other door.")
        print("Because you back tracked ",name+" you have lost 2 star points.")
        SecondroomB(name)
#choice b for the second room/ you choose black door
def SecondroomB(name):
    print()
    print("As you enter the room with different colored lights the door slams shut right behind you.")
    print("You walk around the room filled with light until you see a small white box right in front of you.")
    box(name)
            
# box Q       
def box(name):
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
        pts = 5
        Thirdroom(name)
        return pts
    else:
        print()
        print("You reached already start to open the box only to find it lock.")
        print("You lost 2 star points.")
        print("Looks like you have to find a key now",name+". I have a feeling there is going to be a key in the next room.")
        pts = -2
        Thirdroom(name)
        return pts
        
#thrid room of fun house
def Thirdroom(name):
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
        pts = -5
        Boxq(name)
        return pts
    else:
        print()
        print("You choose the vase filled with Sunflowers. As you take out one of the sunflowers you seemto take the vase with you.")
        print("There is now broken shards of glass but at least you found a key among the scattered sunflowers.")
        print("you have lost 2 star points due to the vase being broken. Sorry about that",name+".")
        print("It was a mistake to have the sunflower vase on the endge of the table.")
        pts = -2
        Boxq(name)
        return pts
#box Q once again
def Boxq(name):
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
        pts = -2
        Finalroom(name)
        return pts
    else:
        print()
        print("Good choice once again",name+".")
        print("You see that the key is too big for the box itself you save it for the last room up ahead")
        print("You get 2 points for not trying the key.")
        pts = 2
        Finalroom(name)
        return pts
#final room of fun house   
def Finalroom(name):
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
        Boxq2(name)

    else:
        print()
        print("The right door is already in vies as you walk towards it.")
        print("WHen you walk out of the room to see the exit sign of the fun house and a small key by the hallway")
        Boxq2(name)

# box Q again
def Boxq2(name):
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
        pts = 10
        Goodbye(name)
        return pts
    else:
        print()
        print("You take one last look at the box and decide to throw it in the trash.")
        print("The box is gone now as well as the key ")
        print("Who knows what was in the box anyway.")
        Goodbye(name)
        return pts
#The final goodbye
def Goodbye(name):
    print()
    print("Thanks for playing my room in the fun house!")
    print("Hopefully you try the other rooms in the game",name+"!")
    return pts
