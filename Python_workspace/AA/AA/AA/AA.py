import sys

res= 0
n = list(map(int,sys.stdin.readline().rstrip()))

n.sort(reverse= True)

for i in range(len(n)):
    res = res * 10 + n[i]
print(res)



#import sys

#sys.stdin = open("input.txt")

#def go(parent, graph, visited):
#    global res
#    visited[parent] = True

#    for child in graph[parent]:
#        if not visited[child]:
#            res[child] = parent
#            go(child, graph,visited)


#n = int(sys.stdin.readline().rstrip())

#graph = [[] for _ in range(n+1)]
#visited = [False]*(n+1)
#res = [None]*(n+1)


#for _ in range(n-1):
#    a, b = map(int, sys.stdin.readline().rstrip().split())
#    graph[a].append(b)
#    graph[b].append(a)

#go(1,graph,visited)

#for i in range(2,n+1):
#    print(res[i])










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