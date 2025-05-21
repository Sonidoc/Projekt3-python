import os
from msvcrt import getwch
import random
from colors import bcolors

wins = 0        #Allt är noll från början förstås.
losses = 0
ties = 0

art = {                         # Asci art som belyser på vad du du valde för något
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



def your_hand():                            # Funktion som frågar dig vad du vill välja för något, du kan också stänga av spelet. Stoppar dig från att skriva något annat än R P S Q som har färger också.
    print("You can always (Q)uit")                     
    print("Which hand:"
    f"{bcolors.BLUE}(R)ock{bcolors.DEFAULT}  "
    f"{bcolors.CYAN}(P)aper{bcolors.DEFAULT}  "
    f"{bcolors.PURPLE}(S)cissors{bcolors.DEFAULT}\n")
    while True: 
        your_input = getwch().upper() # Istället för input() använder jag getwch. .upper gör sp att vi får bara stora bokstäver.
        if your_input in ['R', 'P', 'S']: 
            print(f"\nYou chose: {your_input}") 
            return your_input
        elif your_input in ['Q']: # Om du skriver Q så stoppas hela programmet.
            os.system('cls')
            exit("Goodbye")
        else:
            os.system('cls') # Den här raderar all text så att du kan vara kan se texten under.
            print("WTF are you doing??? Press R, P or S") # Meddelande som säger till dig att skriva rätt bokstav.

def computer_hand():                                # Slumpmässigt mellan R P S för datorn som ska sen bedömas om det är en vinst, förlust eller lika.
    return random.choice(['R', 'P', 'S'])   

def determine_winner(player, computer): # Global gör så att den får tillgång till hela project3 foldern och sammarbetar med Project3.py.
    global wins, losses, ties  

    print("\nYour hand:")                       #Visar vad du och datorn valde för något.
    print(art[player]) #skriver ut händerna som syns ovan all kodblock.
    print("Computer hand:")
    print(art[computer])

    if player == computer:                  # Om det är samma bokstav så blir det lika, vi jämför här så darför ==.
        ties += 1
        return f"{bcolors.YELLOW}It's a tie!{bcolors.DEFAULT}"
    
    if (player == 'R' and computer == 'S') or \
       (player == 'P' and computer == 'R') or \
       (player == 'S' and computer == 'P'):
        wins += 1
        return f"{bcolors.GREEN}You win!{bcolors.DEFAULT}" # Kombinationer som gör så att du vinner, om dessa kravs inte uppyfylls förlårar du.
    else:
        losses += 1
        return f"{bcolors.RED}You lose.{bcolors.DEFAULT}"

def get_stats(): # Ger resultat till project3.py
    global wins, losses, ties  
    return wins, losses, ties