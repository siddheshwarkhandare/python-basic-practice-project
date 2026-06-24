# we need to track how many gussse was right 
import random
user_win=0
computer_win=0
draw=0

option=["rock","paper","scissor"]

while True:
    user_input=input("type rock/paper/scissor or press Q for quite! ").lower()
    if user_input == "q":
        break
    if user_input not in option:
        continue
    """while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue"""
    random_number= random.randint(0,2)
    #    0 rock     1 paper     2 scissor
     
    computer_gusse=option[random_number]
    print("computer pick",computer_gusse+".")

    if user_input=="rock" and computer_gusse=="scissor":
        print("you won")
        user_win+=1

    elif user_input=="paper" and computer_gusse=="rock":
        print("you won")
        user_win+=1

    elif user_input=="scissor" and computer_gusse=="paper":
        print("you won")
        user_win+=1

    elif user_input == computer_gusse:
        print("game is draw")
        draw+=1
    if draw==True:
        print("you lost")
        computer_win+=1
        continue

    print("you won ",user_win,"times")
    print("computer won",computer_win,"times")
    print("draw",draw)