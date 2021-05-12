T = int(input())
for i in range(T):
    N, s, e, k = map(int,input().spit())

slicing=num[s:e+1]
slicing.sort()
print("#",i," ",end="")
print(slicing[k-1])