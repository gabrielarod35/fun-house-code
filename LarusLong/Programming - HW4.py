  # Fun house game

def carlasRoom(name):

    dp = 0

    print("Welcome to my room in the fun house,",name+"!")
    print("Let's get started")

    print("There are two boxes. One with a baby kitten.")
    print("One with a lion.\n")

    print("They are called 1 and 2.")
    print("You may choose not to open any box, ")
    print("but the kitten will reward many points.\n")
    answer = input("Which box do you choose, 1 or 2, or something else? ")

    if answer == "1":
        print("You've been eaten enough to lose 10 pts. ")
        pts = -10
  
    if answer == "2":
        print("The kitten give you 50 points. ")
        pts = 50
  
    print("You are moving on to the next room.")

    return pts


def golfRoom(name):

    dp = 0

    print("Welcome to the golf room in the fun house,",name+"!")
    print("Let's get started")

    print("There are three golf balls in the room. One white golf ball")
    print("One yellow ball.")
    print("One green golf ball.\n")

    print("They are called 1,2 and 3.")
    print("You'll need to choose one ball")
    print("The yellow ball will give you most of the points.\n")
    answer = input("Which golf ball do you want to choose, 1, 2 or 3? ")

    if answer == "1":
        print("You've chosen the white bolf ball that will not give you any points")
        pts = 0

    if answer == "2":
        print("You've chosen the green golf ball and you'll lose this golf ball on the golf course, you'll lose 20 point for that.")
        pts = -20

    if answer == "3":
        print("You've chosen the yellow ball that you'll never lose on the golf course, you'll get 50 points.")
        pts = 50

    print("You are moving on to the next room.")

    return pts
        



def main():

    # get name
    name = input("What is your hero's name? ")

    # initialize points
    points = 0

    print("You are entering the fun house!")

    # first room
    dp = carlasRoom(name)  # dp is the number of points to add or subtract from the point total
    points = points + dp

    # second room
    dp = golfRoom(name)
    points = points + dp
