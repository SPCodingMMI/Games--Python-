import random
import os
import time

GameON = True

def DisplayUserChoice(UserChoice):
    if(UserChoice == 1):
        Result = "You Chose Rock.\n"
        return Result
    elif(UserChoice == 2):
        Result = "You Chose Paper.\n"
        return Result
    elif(UserChoice == 3):
        Result = "You Chose Scissors.\n"
        return Result

def DisplayCPUChoice(CPUChoice):
    if(CPUChoice == 1):
        Result = "CPU Chose Rock.\n"
        return Result
    elif(CPUChoice == 2):
        Result = "CPU Chose Paper.\n"
        return Result
    elif(CPUChoice == 3):
        Result = "CPU Chose Scissors.\n"
        return Result
    
while(GameON):
    print("WELCOME TO ROCK-PAPER-SCISSORS")
    print("******************************")
    Options = str(input("Do You Want To Play? (Y/N) \n"))

    if((Options == "y") or (Options == "Y")):
        UserChoice = int(input("Rock, Paper, or Scissors? \n"))
        CPUChoice = random.randint(1, 3)
        print(DisplayUserChoice(UserChoice))
        time.sleep(2)
        print(DisplayCPUChoice(CPUChoice))
        time.sleep(2)

        if(UserChoice == CPUChoice):
            print("IT'S A TIE!\n")
            continue
        elif(UserChoice == 1):
            if(CPUChoice == 2):
                print("You Lose!\n")
            else:
                print("You Win!\n")
        elif(UserChoice == 2):
            if(CPUChoice == 3):
                print("You Lose!\n")
            else:
                print("You Win!\n")
        elif(UserChoice == 3):
            if(CPUChoice == 1):
                print("You Lose!\n")
            else:
                print("You Win!\n")
    
    elif((Options == "n") or (Options == "N")):
        GameON = False

        
print("Shutting Game Down")
time.sleep(2)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)
print("Shut Down Complete")
time.sleep(3)
os.system('clear')
