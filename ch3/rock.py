# program to play a game of scissors,paper, rock with a computer
#
#-computer makes a random choice.
#-prompts user to make a choice.
# - compare
#- evaluate and determin if tie ; computer or user wins
#- print winner
# end the program

import random
# computer selects random number between 0-2
random_choice = random.randint(0,2)
computer_choice =''
winner =''

# turn the computer's choice into human readable form
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

#prompt the user for input check for valid response
user_choice =''


while (user_choice != 'rock' and 
        user_choice != 'paper' and
        user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? ')
        
        
#check if both chose the same value. If true it is a tie.
if computer_choice == user_choice:
    winner = 'Tie'
 # apply the rules:
 # paper beats rock
 # scissors beats paper
 # rocks beats scissors  
 # evaluate form the computer's perspective 
elif computer_choice == 'rock'and user_choice != 'paper':
    winner='Computer'
elif computer_choice =='paper' and user_choice != 'scissors':
    winner='Computer'

elif computer_choice =='scissors' and user_choice != 'rock':
    winner='Computer'
# no luck for the computer User wins
else:
    winner = 'User'
# Print the results

if winner == 'Tie':
    print('We both chose', computer_choice + ', play again.')
else:
    print(winner,'won. The computer chose', computer_choice + '.')
