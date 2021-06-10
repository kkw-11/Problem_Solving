import sys
sys.stdin = open("input.txt","rt")

list1 = []
list2 = []
list3 = []
n1 = int(input())
list1 = list(map(int,input().split()))
n2 = int(input())
list2 = list(map(int,input().split()))


i = 0
j = 0
while i < n1 and j < n2:
    if list1[i] < list2[j]:
        list3.append(list1[i])
        i += 1
    else:
        list3.append(list2[j])
        j += 1

#while i <n1:
#    list3.append(list1[i])
#    i +=1
#while j < n2:
#    list3.append(list2[j])
#    j+=1

#파이썬스러운 코드
if i < n1:
    list3 = list3 + list1[i:]

if j < n2:
    list3 = list3 + list2[j:]

for x in list3:
    print(x,end=" ")


# import sys
# #sys.stdin = open("input.txt","rt")

# list1 = []
# list2 = []
# list3 = []
# n1 = int(input())
# list1 = list(map(int,input().split()))
# n2 = int(input())
# list2 = list(map(int,input().split()))

# list3 = list1 + list2

# list3.sort()

# for x in list3:
#     print(x,end=" ")
