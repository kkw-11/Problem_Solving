# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    b_start_index = None
    if 'a' and 'b' in S:
        for index in range(len(S)):
            if S[index] == 'b':
                b_start_index = index
                break
        if 'a' in S[b_start_index:]:
            return False

    return True
    

