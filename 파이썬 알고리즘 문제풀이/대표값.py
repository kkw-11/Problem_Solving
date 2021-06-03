import sys
sys.stdin = open("input.txt","rt")

n = int(input())
grade = list(map(int, input().split()))

avg = int(sum(grade)/n + 0.5)
min = 2147000000
for idx in range(n):
    delta = abs(grade[idx] - avg)
    if delta < min:
        min = delta
        minNum = idx + 1
        maxGrade = grade[idx]
    elif delta == min:
        if grade[idx] > maxGrade:
            maxGrade = grade[idx]
            minNum = idx + 1

print(avg, minNum)


# import sys
# #sys.stdin = open("input.txt","rt")

# n = int(input())
# grade = list(map(int,input().split()))
# delta = [0]*len(grade)
# cnt = 0
# minNum = 9999999
# avg = 0
# sum = 0
# for i in range(len(grade)):
#    sum += grade[i]



# avg = int(sum/n + 0.5)
# #print(avg)

# min = float('inf')
# for i in range(len(grade)):
#    delta[i] = abs(grade[i] - avg)
#    if(delta[i]< min):
#        min = delta[i]

# #print(min)

# for i in range(len(grade)):
#    if(min == delta[i]):
#        cnt += 1
#        if cnt>1:   #최소 차이의 점수인 곳이 하나 더 있다면 점수를 비교
#            if temp <grade[i]:
#                temp = grade[i]
#                minNum = i                
#        else:
#            temp = grade[i]
#            minNum = i
    
# print(avg, minNum+1)