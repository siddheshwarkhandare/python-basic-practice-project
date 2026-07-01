#here are problem steament we devlopinng an game that has following requirment 
#user roll a dice 
#if user get any point other than 1  we add that point in to there total score 
# if user get 1 than the score will end and total score will get add to the final score 
#user can dicide how many time they have to roll the dice


# step first roling the dice 
import random

def roll():
    return random.randint(1,6)

while True:
    player=input("welcome to the game, how many plarer in the game (2-4)! ")
    if player.isdigit():
        players=int(player)
        if 2<= players <= 4:
            break
        else:
            print("players must be between 2 to 4")
    else:
        print("enter valide input")

max_score=50
players_list = [ 0 for _ in range(players)]

while max(players_list) < max_score:
    for player_idx in range(players):# it move to next player as per user input 
        print("\n player number ",player_idx+1,"is started")
        current_score=0
        while True:
            user_action=input("would you like to roll(y)! ").lower()
            if user_action != "y":
                break
            value=roll()

            if value == 1:
                current_score=0
                print("you roll 1 your turn done ",current_score)
                break
            else:
                current_score+=value
                print("you roll a ",value)
            print("your score is ",current_score)
        players_list[player_idx]+=current_score# it add the current score to previus score
        print("your total score is ",players_list[player_idx])
max_score=max(players_list)
wining_idx=players_list.index(max_score)