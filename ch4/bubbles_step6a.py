# chapter4 lists and iteration
# given a list of scores
#- output the test and score results
# iterate or the list using a for loop
# find out which test(s) have the best score
# calculate the best cost amonst the best scores
# calculate the most effective  cost more efficiently



scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25,
         .33, .31, .25, .29, .27, .22,
         .31, .25, .25, .33, .21, .25,
         .25, .25, .28, .25, .24, .22,
         .20, .25, .30, .25, .24, .25,
         .25, .25, .27, .25, .26, .29]

length = len(scores)
high_score=0

for i in range(length):
    print('Bubble solution #',str(i),'scores:',scores[i])
    if scores[i] > high_score:
        high_score=scores[i]
print('Bubbles tests:',length)
print('Higheste bubles score:', high_score)

best_solutions=[]

for i in range(length):
    if scores[i] == high_score:
        best_solutions.append(i)

print('Solutions with the highest scores are:',best_solutions)

cost= 100.0
most_effective  = 0


for i in range(len(best_solutions)):
    index = best_solutions[i]
    if costs[i] < cost:
        most_effective = index
        cost =  costs[i]

print('Soulution',most_effective, 'is the most effective with a cost of',costs[most_effective])


     


