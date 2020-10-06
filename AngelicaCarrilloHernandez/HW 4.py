from graphics import *
def angelicasroom(name):
    points = 0
    
    print("Welcome to my room,",name+"!")
    print("By entering this room, you have activated a BOMB!") 
    print("There are only two wires, RED and BLUE")
    print("You have to disconnect one wire from the bomb in order to deactivate it, but you only have 2 minutes")
    print("If you choose the correct wire, You will be rewarded 50 points")
    print("Otherwise, you will loose 10 points. ")

   
    answer = input("Which wire do you want to disconnect, the RED or the BLUE wire?  ")
    if answer == "Red":
        print("CONGRATULATIONS! ")
        print("You have chosen the CORRECT wire! ")
        dp = 50
    if answer == "Blue":
        print("Oops, you have chosen the wrong wire. ")
        print("Now the bomb accelerated and it exploded!" )
        print("You lose 10 points")
        dp = -10
    print("You are now moving to the next room.")

    points = points + dp
    

    return dp 
    

    
