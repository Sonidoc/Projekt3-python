import os
from msvcrt import getwch
import random
from colors import bcolors

wins = 0
losses = 0
ties = 0

art = {
    'R': r"""
  _________
  |   |  |  \__
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \____ROCK_____/
""",
    'P': r"""
    __ __ __
   |  |  |  |__
   |¨¨|¨¨|¨¨|  |
__ |¨¨|¨¨|¨¨|¨¨|
\ \|  |  |  |¨¨|
|  \__         |
|              |
 \____PAPER____/
""",
    'S': r"""
 __       __
 \  \   /  /
  \  \ /  /
   \  V  /__ __
  /¨¨¨¨===  |  |
 /    ___/__|__|
|    /         |
 \__SCISSORS___/
"""
}



def your_hand():
    print("You can always (Q)uit")
    print("Which hand:"
    f"{bcolors.BLUE}(R)ock{bcolors.DEFAULT}  "
    f"{bcolors.CYAN}(P)aper{bcolors.DEFAULT}  "
    f"{bcolors.PURPLE}(S)cissors{bcolors.DEFAULT}\n")
    while True: 
        your_input = getwch().upper()
        if your_input in ['R', 'P', 'S']:
            print(f"\nYou chose: {your_input}")
            return your_input
        elif your_input in ['Q']:
            os.system('cls')
            exit("Goodbye")
        else:
            os.system('cls')
            print("WTF are you doing??? Press R, P or S")

def computer_hand():
    return random.choice(['R', 'P', 'S'])   

def determine_winner(player, computer):
    global wins, losses, ties  

    print("\nYour hand:")
    print(art[player])
    print("Computer hand:")
    print(art[computer])

    if player == computer:
        ties += 1
        return f"{bcolors.YELLOW}It's a tie!{bcolors.DEFAULT}"
    
    if (player == 'R' and computer == 'S') or \
       (player == 'P' and computer == 'R') or \
       (player == 'S' and computer == 'P'):
        wins += 1
        return f"{bcolors.GREEN}You win!{bcolors.DEFAULT}"
    else:
        losses += 1
        return f"{bcolors.RED}You lose.{bcolors.DEFAULT}"

def get_stats():
    global wins, losses, ties  
    return wins, losses, ties