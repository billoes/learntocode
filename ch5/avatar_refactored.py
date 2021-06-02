#A new startup around the corner has been working on some code to help
#their users choose an avatar.They’ve just started, and so far all their code does is ask for
# the user’s preferences for hair color, eye color, gender, and so on—once they get
#this all working, they’ll presumably take all these preferences and generate a
#nice avatar image for each user.

# using  a function to abstract the code

def get_attribute(query,default):
    answer = input(query+"["+ default +"]?")
    if answer=='':
        answer= default
    print('You chose ',answer)
    return answer



# use the function get_avatar to get answers

hair = get_attribute('What hair color', 'brown')
hair_length = get_attribute('What hair length', 'short')
eye = get_attribute('What eye color', 'blue')
gender = get_attribute('What gender', 'female')
glasses = get_attribute('Has glasses', 'no')
beard = get_attribute('Has beard', 'no')

print('your avatar: has',hair,hair_length,'hair',eye,'eyes','a',gender,'wears glasses',glasses,'has a beard',beard)

