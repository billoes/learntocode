#This is a short guessing game
#
color = 'blue'
guesses = 0
guess = ''

#increment the count of guesses after an incorrect guess
while guess != color:
    guess = input('What color am I thinking of ? ')
    guesses = guesses + 1
if guesses == 1:
    print('You guessed the color in 1 try.')
else:
    print('You got it! It took you', guesses,'guesses')



