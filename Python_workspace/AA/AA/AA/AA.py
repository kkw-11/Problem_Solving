import sys
from collections import deque

sys.stdin = open("input.txt")

N, K = map(int,sys.stdin.readline().rstrip().split())

check = [False]*(N+1)
check[0] = True

q = deque()
res = []
cnt = 0
for i in range(1,N+1):
    q.append(i)

while q:
    for i in range(K):
        num = q.popleft()
        if i == K-1:
            res.append(num)
        else:
            q.append(num)



print("<",end="")
for i in range(N-1):
    print(res[i],end="")
    print(", ",end="")
else:
    print(res[N-1],end="")
    print(">",end="")



#import sys
#import math

#sys.stdin = open("input.txt")

#n, m = map(int,sys.stdin.readline().rstrip().split())

#print(n,m)

#chessboard = []
#min_result = math.inf
#temp = None
#cnt = 0
#res = [[0]*m for _ in range(n)]

#for i in range(n):
#    input = sys.stdin.readline().rstrip()
    
#    chessboard.append(list(input))
    
#    #chessboard[i] = input


##for c in chessboard:
##    print(c)



#for startRow in range(n-7):
#    for startCol in range(m-7):
#        temp = chessboard
#        cnt = 0

#        if temp[startRow][startCol] == 'B':

#            for i in range(startRow,startRow+7):
#                for j in range(startCol, startCol+7):
#                    pass
            

#            temp = chessboard
#            temp[startRow][startCol] = 'W'
#            res[startRow][startCol] = cnt
#            cnt = 0
#            for i in range(startRow,startRow+7):
#                for j in range(startCol, startCol+7):
#                    pass

#            if res[startRow][startCol] > cnt:
#                res[startRow][startCol] = cnt

#for startRow in range(n-7):
#    for startCol in range(m-7):
#        print(res[startRow][startCol], end= " ")
#    print()