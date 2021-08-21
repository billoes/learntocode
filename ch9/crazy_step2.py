# Crazy Libs
#Pseudo code
# Start with creating a template - contains text with placeholderfor NOUN,VERB,and ADJECTIVE inside the text 
# 1-Read the text file "lib.txt" from file.
#
#2 -Process the text.
#   	A if word is a placeholder (NOUN,VERB, VERB_WITH_ING or ADJECTIVE)
#        		1 Prompt user for a placeholder part of speech.
#       		2 Substitute user's word for the placeholder. 
#   	B- Otherwise the word is fine; keep it in the story.
# 3- Store results
# Take the processed text with the placeholders filed and write it out to a file 
# with the name prepended by "crazy__" .

def make_crazy_lib(filename):
    file = open(filename, 'r')
    text = ''

    for line in file:
        text = text + process_line(line)
    file.close()
    return text

placeholders = ['NOUN', 'ADJECTIVE', 'VERB_ING', 'VERB']

def process_line(line):
    global placeholders
    processed_line = ''
    
    words = line.split()
    
    for word in words:
        if word in placeholders:
            answer = input('Enter a ' + word + ":")
            processed_line = processed_line + answer + ' '
        else:
            processed_line = processed_line + word + ' '
    

    return processed_line + '\n'


def main():
    lib = make_crazy_lib('./ch9/lib.txt')
    print(lib)

if __name__ == '__main__':
    main()


