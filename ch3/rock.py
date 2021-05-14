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
winner ='it is a tie'



print ('The computer choses', random_choice)
if random_choice == 0:
    computer_choice = 'rock'
elif random_choice == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'
print ('The computer chose', computer_choice)

user_choice = input('rock, paper or scissors? ')
print('You chose', user_choice, 'and the computer chose', computer_choice)

if computer_choice == user_choice:
    winner = 'it is a tie'
 #   print('it is a tie.')
elif computer_choice == 'rock'and user_choice != 'paper':
    winner='computer'
elif computer_choice =='paper' and user_choice != 'scissors':
    winner='computer'

elif computer_choice =='scissors' and user_choice != 'rock':
    winner='computer'
#elif computer_choice == user_choice:
#    winner ='it is a tie'     
else:
    winner = 'you'

print('The winner is,', winner,'.')