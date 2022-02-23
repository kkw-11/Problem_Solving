def solution(number, k):
    answer = ''
    stack = []

    for cur_num in number:
        while k and len(stack) != 0 and stack[-1] < cur_num :
            stack.pop()
            k -= 1
        stack.append(cur_num)

    if k:
        answer = "".join(stack[:-k])
    else:
        answer = "".join(stack)

    return answer