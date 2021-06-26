from collections import deque, defaultdict

def isOneCharDiffer(str1, str2):
    differCnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            differCnt += 1

        if differCnt == 2:
            return False
    else:
        if differCnt == 1:
            return True


def solution(begin, target, words):
    answer = 0
    wordLen = len(begin)
    stage = 0
    
    # 한글자 차이나는 글자들로 그래프 만들기
    wordGraph = defaultdict(list)
    usedWord = defaultdict(bool)
    for word1 in words:
        if isOneCharDiffer(begin,word1):
            wordGraph[begin].append(word1)
        
        for word2 in words:
            if isOneCharDiffer(word1,word2):
                wordGraph[word1].append(word2)
                usedWord[word1] = False
                
    print(wordGraph)
    if target not in words:
        answer = 0
        return answer
    else:

        if isOneCharDiffer(begin, target):
            answer = 1
            return answer
        else:
            queue = deque()
            queue.append([begin,0])
            while queue:
                curWord, cnt = queue.popleft()

                if curWord == target:
                    return cnt

                for word in wordGraph[curWord]:
                    if not usedWord[word]: # 단어 사용하지 않았다면 
                        queue.append([word,cnt +1])
                        usedWord[word] = True
                    
        
    return answer


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
