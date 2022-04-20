from itertools import product
def solution(word):
    answer = 0
    vowels = ['A','E','I','O','U']
    all_words = []
    words_sequence = {}
    for i in range(1,6):
        print(i)
        all_words.extend(list(product(vowels, repeat=i)))
    
    all_words.sort()
    print(all_words[0])
    for seq, word_value in enumerate(all_words):
        if "".join(word_value) == word:
            return seq + 1
    
    return answer