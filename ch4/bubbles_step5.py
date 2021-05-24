# chapter4 lists and iteration
# given a list of scores
#- output the test and score results
# iterate or the list using while count<length
#bubble report summary
# 
# after listing the scores summarize:
# varibles highest=0; tests=[] 
# total number of test: Length of the list of test
# highest score: start with highest=0 compare if highest greater then
# test if no replace highest with present score, iterate to the end of list.
# Iterate throug the list with the highest score add equal scores to tests list
# 
# show higest score 
# show tests
#
scores = [60, 50, 60, 58, 54, 54, 58, 50, 52, 54, 48, 69,
          34, 55, 51, 52, 44, 51, 69, 64, 66, 55, 52, 61,
          46, 31, 57, 52, 44, 18, 41, 53, 55, 61, 51, 44]
i=0
length = len(scores)
highest= 0
tests = []

while i< length:
    print('Bubble solution #',str(i),'scores:',scores[i])
    i= i+1

print('Number of tests:',length)

i=0
while i< length:
    
    if highest < scores[i]:
        highest = scores[i]
    i = i +1
        
print('highest score is',highest)


i=0

while i<length:
    if highest == scores[i]:
        tests.append(i)
    i=i+1
print('The tests with the highest scores are:',tests)
