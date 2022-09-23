import random

def play():
    #input takes whatever the user says as gospel. Has to be exact. Don't code trying to limit it.
    player_choice = input("What's your choice? 'r' for rock,'p' for paper,'s' for scissors\n")
    computer_guess = random.choice(['r', 's', 'p']) #Make sure to put single quotes/bracket for character choices

    if player_choice == computer_guess: # got this correct
        return 'tie' 
    if is_win(player_choice, computer_guess):
        return 'You won!'
    return 'You lost!'

def is_win(player, computer): #define veriables like in Matlab functions
    if (player == 'p' and computer =='r') or (player == 's' and computer == 'p') \
         or (player == 'r' and computer == 's'): #logic like VHDL. Parenthesis are must
         return True

#This block I created isn't even needed! THINK THE LAST CONDITION IS I LOST TO SAVE CODE!!
#def is_lose(player, computer):
    #if (player == 'r' and computer =='p') or (player == 'p' and computer == 's') \
        # or (player == 's' and computer == 'r'): #logic like VHDL. Parenthesis are must
        #return True

print(play())

#Addition to this
#if I wanted to identify which choice I lost to, I could create conditionals based on each with a print statement saying how I lost.