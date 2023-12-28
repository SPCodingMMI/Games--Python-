import random
import os
import time

GameON = True

while(GameON):
    print("WELCOME TO THE GUESSING NUMBER GAME!")
    print("************************************")
    print("Do you want to play?")
    UserChoice = str(input())
    
    if((UserChoice == "y") or (UserChoice == "Y")):
        UserNum = int(input("Enter Your Number: "))
        RandNum = random.randint(1, 10)
        Count = 1
        if(UserNum == RandNum):
            print("You Win!")
            print("You did it on your first try!")
        while(UserNum != RandNum):
            Count += 1
            UserNum = int(input("Wrong! Enter Your Number: "))
            if(UserNum == RandNum):
                print("You Win!")
                print("It took you " + str(Count) + " tries!\n")
        
    elif((UserChoice == "n") or (UserChoice == "N")):
        print("System...Shutting Down")
        time.sleep(3)
        GameON = False
