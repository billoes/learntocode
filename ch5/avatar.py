#A new startup around the corner has been working on some code to help
#their users choose an avatar.They’ve just started, and so far all their code does is ask for
# the user’s preferences for hair color, eye color, gender, and so on—once they get
#this all working, they’ll presumably take all these preferences and generate a
#nice avatar image for each user.

# here is the old code that needs improvement
hair = input("What color hair [brown]? ")
if hair =='':
    hair= 'brown'
print('You chose' , hair)

hair_length = input("What hair length [short]? ")
if hair_length =='':
    hair_length = 'short'
print('You chose' , hair_length)

eyes = input("What eye color [blue]? ")
if eyes =='':
    eyes = 'blue'
print('You chose' , eyes)

gender = input("What gender [female]? ")
if gender =='':
    gender = 'female'
print('You chose' , gender)

has_glasses = input("Has glasses [no]? ")
if has_glasses =='':
    has_glasses = 'no'
print('You chose' , has_glasses)

has_beard = input("Has beard [no]? ")
if has_beard =='':
    has_beard = 'no'
print('You chose' , has_beard)





