#https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

##파이썬 함수 사용 풀이
from itertools import permutations

def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    else:
        return True

def permu(number):
    a = set()
    for i in range(len(number)):
        a |= set(map(int, map("".join, permutations(number, i + 1))))
    return a
    
    
def solution(numbers):
    answer = 0
    
    # 숫자 문자열 하나씩 뽑아 리스트에 저장
    number = list(numbers)
    #완전 탐색으로 숫자 조합만들기
    a = set()
    
    a |= permu(number)
    #만들어진 숫자 소수인지 판단
    for x in a:
        if isPrime(x):
            answer += 1
    return answer