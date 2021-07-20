# Anti-Social App
# This app finds the user with the fewest number of friends
# The set users are given.
# key is the name, 
# 'email',
# 'gender',
#  'age',
# 
# 'friends'['Name1', 'Name2'] 
# Pseudo code
# 1 Set max to large number 1000
# 2- For each name in users
#       A-Get the attribute dictionary
#       B-Get the list of friends from the attribute dictionary
#       C-If number of friendsis less than max
#           i- set the varible most_snti_social to name
#           ii- set variblr max to number of freiends
# 3- Print user with key moost_anti_social
#
#
#
users = {} 
users['Kim'] = {'email' : 'kim@oreilly.com','gender': 'f', 'age': 27, 'friends': ['John', 'Josh']}
users['John'] = {'email' : 'john@abc.com','gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {'email' : 'josh@wickedlysmart.com','gender': 'm', 'age': 32, 'friends': ['Kim']}

max = 1000

for name in users:
   user = users[name]
   friends = user['friends']
   
   if len(friends) < max:
       most_anti_social = name
       max = len(friends)

print('The most anti-social is', most_anti_social)
