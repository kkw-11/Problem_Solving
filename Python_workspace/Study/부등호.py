
# import sys
# import heapq
# import math
# from collections import deque
# sys.setrecursionlimit(1001*1001)

# n = int(input())
# arr = list(input().split())
# res = []
# ch  = [0]*(11)

# def go(ch,idx,cNum,ans):
#     if idx == n: # 지금까지 3개 넣었다는 의미이다 
#         res.append(''.join(map(str,ans)))
#     else:
#         for i in range(0,10):
#             if ch[i] == 0 :
#                 if arr[idx] == '<' and cNum < i:
#                     ch[i] = 1
#                     go(ch,idx+1,i,ans + [i])
#                     ch[i] = 0
#                 if arr[idx] == '>' and cNum > i:
#                     ch[i] = 1
#                     go(ch,idx+1,i,ans + [i])
#                     ch[i] = 0

# for i in range(0,10):
#     ch[i] = 1
#     go(ch,0,i,[i])
#     ch[i] = 0

# print(res[-1])
# print(res[0])
