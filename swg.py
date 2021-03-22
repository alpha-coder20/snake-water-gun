import random as rd
import time 

print("Snake Water Gun Game") 
print("Press S for Snake")
print("Press W for Water")
print("Press G for Gun")

turns = 0
game = ["S", "W", "G"]
csc=0
usc=0
def myfunc():
    global csc
    csc = csc+1
def myfun():
    global usc
    usc = usc+1
    
def rule(Computer,User):
    if Computer=="S" and User=="W":
        print("Computer won this hand.")
        myfunc()
    elif Computer=="W" and User=="S":
        print("You won this hand.")
        myfun()
    elif Computer=="W" and User=="G":
        print("Computer won this hand.")
        myfunc()
    elif Computer=="G" and User=="W":
        print("You won this hand.")
        myfun()
    elif Computer=="G" and User=="S":
        print("Computer won this hand.")
        myfunc()
    elif Computer=="S" and User=="G":
        print("You won this hand.")
        myfun()
    elif Computer==User:
        print("Tie")
    else:
        print("I did not understand your request")

while turns<10:
    user = (input()).upper()
    comp = rd.choice(game)
    rule(comp,user)
    turns = turns+1

if csc>usc:
    print("Computer Won. Better Luck Next Time.")
elif usc>csc:
    print("Congratulations ! You Won.")
else:
    print("There Was A Tie.")

time.sleep(5)