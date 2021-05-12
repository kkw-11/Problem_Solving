#강의 풀이 시간복잡도와 공간복잡도를 줄일 수 있는 코드
#K번째 약수가 구해지면 break를 해서 K+1번째 약수부터는 굳이 계산하지 않도록 
#코드를 구현하는 것이 시간복잡도를 줄이기에는 더 좋은 코드인다.
import sys
#sys.stdin = open("input.txt","rt")
                 
N,K = map(int,input().split()) #띄어쓰기를 구분으로 읽어 들어와서 N,K에 int형으로 저장

cnt = 0
for i in range(1,N+1):
    if N % i == 0:
        cnt += 1
    if cnt == K:
        print(i)
        break
else:
    print(-1)


        




#import sys
#sys.stdin = open("input.txt","rt")
                 
#N,K = map(int,input().split()) #띄어쓰기를 구분으로 읽어 들어와서 N,K에 int형으로 저장

#num = []
#cnt = 0
#for i in range(1,N+1):
#    if N % i == 0:
#        num.append(i)
#        cnt += 1
        

#if cnt<K:
#    print(-1)
#else:
#    print(num[K-1])


    