# chapter4 lists and iteration
# given a list of scores
#- output the test and score results
# iterate or the list using a for loop


scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]

length = len(scores)
high_score=0

for i in range(length):
    print('Bubble solution #',str(i),'scores:',scores[i])
    if scores[i] > high_score:
        high_score=scores[i]
print('Bubbles tests:',length)
print('Higheste bubles score:', high_score)




    


