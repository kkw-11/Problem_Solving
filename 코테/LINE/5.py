def solution(arr, brr):
   answer = 0
   for i in range(len(arr)-1):
       temp =  (brr[i] - arr[i])
       if temp != 0:
           arr[i] = brr[i]
           arr[i+1] = arr[i+1] - temp
           answer += 1

   return answer

print(solution([3, 7, 2, 4], [4, 5, 5, 2]))
# 4 5 5 2















# def solution(abilities, k):
#     answer = 0
#     difs = []
#     if len(abilities) % 2 == 1:
#         abilities.append(0)
#     abilities.sort(reverse=True)

#     for i in range(0,len(abilities)-1,2):
#         difs.append((abilities[i]-abilities[i+1],abilities[i],abilities[i+1]))
#     difs.sort(reverse=True)

#     for dif in difs:
#         if k>0:
#             k -= 1
#             answer += dif[1]
#         else:
#             answer += dif[2]

#     return answer

# abilities = [2, 8, 3, 6, 1, 9, 1, 9]
# k = 2









# def solution(abilities, k):
#     answer = 0
#     difs = []
#     if len(abilities) % 2 == 1:
#         abilities.append(0)
#     abilities.sort(reverse=True)

#     for i in range(0,len(abilities)-1,2):
#         difs.append((abilities[i]-abilities[i+1],abilities[i],abilities[i+1]))
#     difs.sort(reverse=True)

#     for dif in difs:
#         if k>0:
#             k -= 1
#             answer += dif[1]
#         else:
#             answer += dif[2]

#     return answer

# abilities = [2, 8, 3, 6, 1, 9, 1, 9]
# k = 2

