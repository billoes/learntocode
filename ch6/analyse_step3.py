import ch1text
def count_sentences(text):
    count =0
    for char in text:
        if char == '.' or char == ';' or char == '?' or char == '!':
            count = count +1
    
    return count

def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0

    words =text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    
    print(total_words, 'word')
    print(total_sentences, 'sentences')
    

compute_readability(ch1text.text)



