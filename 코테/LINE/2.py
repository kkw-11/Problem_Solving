from itertools import combinations

def solution(sentences, n):
    answer = 0
    all_char = {}
    for sentence in sentences:
       
        char_dict = {}
        score = 0
        score += len(sentence)
        for char in sentence:
            if char != ' ':
                char_dict[char.lower()] = True
                all_char[char.lower()] = True
            if char.isupper():
                char_dict["shift"] = True
                all_char["shift"] = True
                score += 1
        print(char_dict.keys())
        print(score)
    print(all_char.keys())
    print(list(combinations(all_char.keys(),n)))

    return answer

sentences = ["line in line", "LINE", "in lion"]
n = 5
solution(sentences, n)

