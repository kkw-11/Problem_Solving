import sys

def recur(n):
    if n == 1 or n == 2:
        dy[n] = n
        return dy[n]
    else:
        if dy[n] == 0:
            dy[n] = recur(n-1) + recur(n-2) 
        return dy[n]

n = int(input())
dy = [0]*(n+1)

print(recur(n))


# import sys

# def recur(n):
#     if n == 1 or n == 2:
#         dy[n] = n
#         return dy[n]
#     else:
#         if dy[n] > 0:
#             return dy[n]
#         else:
#             dy[n] = recur(n-1) + recur(n-2) 
#             return dy[n]

# n = int(input())
# dy = [0]*(n+1)

# print(recur(n))