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

def process_line(line):
    return line

def main():
    lib = make_crazy_lib('./ch9/lib.txt')
    print(lib)

if __name__ == '__main__':
    main()


