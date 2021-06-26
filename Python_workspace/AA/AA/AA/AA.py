from collections import deque
    
def bfs(begin,target,words,check):
    # begin으로 시작
    q = deque()
    q.append((begin,0))
    while q :
        wd,cnt = q.popleft()
        if wd == target : return cnt
        # 그냥 매번 모든 단어에 대해서 조사하자
        for i in range(len(words)) :
        # arr = [1,2,3,4]
        # for i in range(len(arr)) : print(arr[i])
            if len([j for j in range(len(words[i])) if words[i][j] != wd[j]]) == 1 and check[i] == 0 :
                check[i] = 1
                q.append((words[i],cnt+1))
    
def solution(begin, target, words):
    # bfs
    # 왜냐하면 "최소 몇단계의 과정" 이라고 물어봤기 때문이다
    # 그렇다면, 정점의 정의는 당연히 각각의 단어가 될 것이다
    # check 배열도 따로 존재해야 할 것 같다
    if target not in words : return 0
    check = [0] * len(words)
    return bfs(begin,target,words,check)


print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
