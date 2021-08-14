import sys

res = set()
nums = []

def subSet(depth, sum, n, nums):

    if depth == n:
        res.add(sum)
        return 

    sum += nums[depth]
    subSet(depth+1,sum, n, nums)
    
    sum -= nums[depth]
    subSet(depth+1,sum, n, nums)

#sys.stdin = open("input.txt")
    
n = int(sys.stdin.readline().rstrip())

nums = list(map(int,sys.stdin.readline().rstrip().split()))

subSet(0,0,n,nums)

res = list(res)
res.sort()
for i in range(len(res)):
    if res[i] != i:
        print(i)
        break
else:
    print(res[-1]+1)


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