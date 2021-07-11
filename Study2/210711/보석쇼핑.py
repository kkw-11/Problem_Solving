# https://programmers.co.kr/learn/courses/30/lessons/67258

def solution(gems):
    gemsCategoryCnt = len(set(gems))
    dic = { gems[0]: 1 }
    answer = [1, len(gems)]
    start , end = 0, 0
    
    while(start < len(gems) and end < len(gems)):
        if len(dic) != gemsCategoryCnt:
            end += 1
            if end >= len(gems):
                break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
        else:
            if end - start < answer[1] - answer[0]:
                answer = [start + 1, end + 1]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
    return answer

# def solution(gems):
#     answer = [] 
#     shortest = len(gems)+1 # 현재 최단 구간 길이

#     start = 0 # 구간의 시작점
#     end = 0 # 구간의 끝 점 (보석을 체크하는 기준점)

#     gemsCategoryCnt = len(set(gems)) # 보석의 총 종류 수
#     contained = {} # 현재 구간에 포함된 보석들(종류: 갯수)

#     while end < len(gems): # 구간의 끝 점이 gems의 길이보다 작을 동안

#         if gems[end] not in contained: # 현재 끝 점의 보석이 contained에 없다면(이 종류가 처음 발견되었다면)
#             contained[gems[end]] = 1 # dictionary에 추가
#         else:
#             contained[gems[end]] += 1 # 이미 있으면 dictionary에 +1
            
#         end += 1 # 끝 점 증가

#         if len(contained) == gemsCategoryCnt: # 현재 구간 내 보석의 종류의 갯수가 전체 종류의 갯수와 같다면 (현재 구간내 모든 종류가 다 있다면)
#             while start < end: # start_p 가 end_p 보다 같을 때까지 증가
#                 if contained[gems[start]] > 1: # start_p에 해당하는 보석이 구간 내에 하나 이상 있다면
#                     contained[gems[start]] -= 1 # 구간 내 보석 하나 감소(start_p 의 보석 뺄거니까)
#                     start += 1 # start_p 증가
                    
#                 elif shortest > end - start: # 기존의 구간 최단거리보다 현재의 구간거리가 더 짧다면
#                     shortest = end - start
#                     answer = [start+1, end] # answer와 최단거리 갱신
#                     break
                    
#                 else:
#                     break


#     return answer