def solution(number, k):
    answer = ''
    n = len(number) -k
    number_list = list(number)
    print(sorted(list(map("".join,combinations(number_list,n))))[-1])

    return answer