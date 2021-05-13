# program to play a game of scissors,paper, rock with a computer
#
#-computer makes a random choice.
#-prompts user to make a choice.
# - compare
#- evaluate and determin if tie ; computer or user wins
#- print winner
# end the program
import random

random_choice = random.randint(0,2)
computer_choice =''


print ('The computer chooses', random_choice)
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'
print ('The computer choooses', computer_choice)
