import random

def roll():
    return random.randint(1,6)


def game():
    player_scores = [0,0]
    player = 0 
    round_score = 0

    while max(player_scores) < 100:
        print('Player',{player+1},'turn') 
        pick = input('Do you want to roll (r) or bank (b)? ').lower()   

        if pick ==  'r':
            roll = roll()
            print('You rolled a '+str(roll))

            if roll == 1:
                print('Round over, You rolled a 1.')
                round_score = 0
                player = 1 - player 
            else:
                round_score += roll
    
        elif pick == 'b':
            player_scores[player] += round_score
            print('Player '+str(player + 1)+ 'banked '+str(player_scores[player]))
            round_score = 0
            player = 1 - player 
    
        else:
            print("Not a valid input. Enter 'r' to roll or 'b' to bank")
    
    print("Player "+str(player_scores.index(max(player_scores))+1)+" wins!")

game()