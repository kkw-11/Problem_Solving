#https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True
    hash_map = {}
    
    # 등장한 숫자들을 count 딕셔너리로 만듦
    for phone_number in phone_book:
        hash_map[phone_number] = 1
        
    # 다시 숫자들을 꺼낸뒤
    # 123 1 2 3 
    for phone_number in phone_book:
        temp = ""
        for number in phone_number: #숫자 하나씩 뜯어보기
            temp += number #1235 1 12 123 1235
            #딕셔너리 키로 같은게 있지만! 전체 숫자는 다른 경우!
            if temp in hash_map and temp != phone_number: # 딕셔너리에 키 있는지 확인하기 key in dictionary
                answer = False
                
    # print(hash_map)
    return answer




# def solution(phone_book): 
#     answer = True 
#     phone_book.sort() 
#     print(phone_book)
    
#     for i in range(len(phone_book)-1): 
#         if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: 
#             answer = False 
#             break 
#     return answer

## 효율성 시간초과 코드 배열 리스트끼리의 비교 시간복잡도 안 좋음 
# def solution(phone_book):
#     answer = True
#     # phone_book.sort()
#     # 567, 88 123 12
#     for index, value in enumerate(phone_book):
#         for i in range(index+1,len(phone_book)):
#             if phone_book[i].startswith(value):
#                 return False
    
#     return answer

## 스터디원 코드
# def solution(phone_book): 
#     answer = True 
#     phone_book.sort() 
#     print(phone_book)
    
#     for i in range(len(phone_book)-1): 
#         if phone_book[i] == phone_book[i+1][:len(phone_book[i])]: 
#             answer = False 
#             break 
#     return answer