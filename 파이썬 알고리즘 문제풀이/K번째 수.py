import sys
#sys.stdin = open("input.txt","rt")

T = int(input())
num = []
for i in range(T):
    N, s, e, k = map(int,input().split())
    num = list(map(int,input().split())) # 한줄의 입력 데이터를 공백을 기준으로 데이터를 입력받아 list로 저장
    num = num[s-1:e]
    num.sort()
    print("#",i+1," ",end="")
    print(num[k-1])
    #print("#%d %d" %(i+1,num[k-1])) ##서식지정자로 출력하는 방법



# import sys
# #sys.stdin = open("input.txt","rt")

# T = int(input())
# num = []
# for i in range(T):
#     N, s, e, k = map(int,input().split())
#     num = list(map(int,input().split()))
#     slicing = num[s-1:e]
#     slicing.sort()
#     print("#",i+1," ",end="")
#     print(slicing[k-1])



