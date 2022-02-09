def solution(number, k):
    stack = []
    for cur_num in number:
        while len(stack) != 0 and stack[-1] < cur_num and k > 0:
            stack.pop()
            k -= 1
        stack.append(cur_num)
            
    if k > 0:
        stack = stack[:-k]
        
    return "".join(stack)