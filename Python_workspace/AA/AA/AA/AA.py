import sys

count  = 0

def dfs(depth,sum,n,s,a) :
    if depth >= n :
        return

    if sum+a[depth] == s   :
        global count
        count+=1

    dfs(depth+1,sum,n,s,a)
    dfs(depth+1,sum + a[depth],n,s,a) 


def solve() :
    n,s = map(int,sys.stdin.readline().split())

    global count
    count = 0

    a = list(map(int,sys.stdin.readline().split()))
    dfs(0,0,n,s,a)

    print(count)

if __name__ == "__main__" :
    solve()


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