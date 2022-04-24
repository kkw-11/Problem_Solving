from itertools import product
def solution(word):
    answer = 0
    vowels = ['A','E','I','O','U']
    all_words = []
    words_sequence = {}
    
    for i in range(1,6):
        # 5 + 5^2 + 5^3 + 5^4 + 5^5 = 5 + 25 + 125 + 625 + 3125 = 780 + 3125 = 3905
        for st in product(vowels, repeat=i):
            all_words.append("".join(st))
    
    all_words.sort() # 3905*log3905 = 3905*(3.xx) = 11715
    answer = all_words.index(word) + 1
   
    return answer