from collections import deque, defaultdict

def isOneCharDiffer(str1, str2):
    charDifferCnt = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            charDifferCnt += 1
            if charDifferCnt >=2:
                return False
    else:
        if charDifferCnt == 1:
            return True     
            
            
def solution(begin, target, words):
    answer = 0
    
    
    if target not in words:
        answer = 0
        return answer
    else:
        if isOneCharDiffer(begin,target):
            answer = 1
            return answer

        # Graph 생성
        wordGraph = defaultdict(list)
        usedWord = defaultdict(bool)

        for word1 in words:
            if isOneCharDiffer(begin,word1):
                wordGraph[begin].append(word1)

            for word2 in words:
                if isOneCharDiffer(word1,word2):
                    wordGraph[word1].append(word2)
                    usedWord[word1] = False
        
        # BFS 탐색
        q = deque()
        
        q.append([begin,0]) #[word,stage]
        
        while q:
            curWord, stage = q.popleft()
            
            if curWord == target:
                answer = stage
                return answer
            
            for nextWord in words[curWord]: # 현재 단어와 연결된 단어 nextWord에 담기
                if not usedWord[nextWord]:
                    usedWord[nextWord] = True
                    q.append([nextWord,stage + 1])

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))

    
