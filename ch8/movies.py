movies = []
movie ={}

movie['name'] = 'Forbidden Planet'
movie['year'] = 1957 ,
movie['rating'] = '****'

movies.append(movie)
movie2 = {'name': 'I was a teenage Werewolf', 'year': 1957, 'rating': '****'}
movie2['rating'] = '***'

movies.append(movie2)
movies.append({'name': 'Viking men and the Sea Serpent',
                'year': 1957 ,
                'rating': '**'})
movies.append({'name': 'Vertigo' ,
                'year': 1957 ,
                'rating': '*****'})

print('Head First Movie Reccomendtions')
print('---------------------------')
for movie in movies:
    if len(movie['rating']) >= 4:
        print(movie['name'], '(' + movie['rating'] + ')', movie['year'])
