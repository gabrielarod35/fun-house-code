# HW 4: Functions and Decision Structures

**Note on runningn on Repl.it:**

The first time you run this in Repl.it, you need to start python in the right pane by typing ```python``` at the prompt.
This should get you running python in your project "directory."

Once you've done that, you should be able to type ```from main import *``` 
to read your file called main.py.
You're free to write your function in main.py, though if  you choose a different
file name, you'll need a different command.
For example, if your file is called thisFile.py, then you'll have to run
```
from thisFile import *
```
to read in its contents.

Finally, after starting python and reading the contents of your file, you'll
be able to call the functions you've written in your file.
If you change your file, you'll need to type the import command again.
If you do and Repl.it doesn't seem to find your changes, hit the arrow button
again, start python (type ```python```again), and reenter the import command.


**Running on IDLE:**

If you're running on IDLE, simply open a file in IDLE, such as ```main.py```, and run the module (key F5).
Then you should be able to run any functions you've defined in that file.

**Running on Colaboratory:**

Since there are no graphics in this assignment, you can also download the file
to your computer and upload to Colaboratory.
If you do, just remember to upload your final version back to your GitHub 
repostory.

---


# Fun House Room

This homework was begun together in the class of Sep 28.
See the recorded lecture for more information.

## Problem statement

Let's write a text-based game in which our hero is walking through a fun house.  We'll start in a function called ```main()```, but each room into which the hero enters will have action handled by its own function.

Each of you will write the function for one room, and then we'll combine them.  Requirements you need to follow:
- Upon beginning your function, print out a description of the room.
- Each room will contain a game the hero can play for points, and you'll need to pass the number of points earned or lost back to the main function.
- Use **decision structures** to play the game and assign the points.

Below is a skeleton of  the function that will call your codes,
room by room, just to get us going.

```Python
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
  dp = abdulsRoom(name)
  points = points

```
