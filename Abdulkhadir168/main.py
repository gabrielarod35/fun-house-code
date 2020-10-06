
def main():
  name = input("What is your hero's name? ")

  points = 0
 
  dp = Abdul's room(name)
  points = points + dp
  print("Welcome to the hardest level in the game,",name+"!")
  Print("Your challenge begins!")
  Print("There are 2 Chests in this room one is ruby the next is sapphire")
  Print("Beware a ghost lives in one which sends you back to the previous room -30 points")
  Print("the other has a key to send you to the next room +60 points)
  Input("which gem shaped chest do you choose? ruby or sapphire")
  answer = input("which gem shaped chest do you choose? ruby or sapphire")
  if answer == "ruby":
   print("Tough luck return to where you came from, -30 points")
   points = -30
  if answer == "sapphire":
   Print("You got lucky you just found the key, +60 points")
   points = +60
   Print(" advance to the next room")
   return points
