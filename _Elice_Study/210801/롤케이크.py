import sys
import heapq
n, m = map(int,sys.stdin.readline().rstrip().split())

cakes = list(map(int, sys.stdin.readline().rstrip().split()))

ten_multi_cake = []
not_ten_multi_cake = []
answer = 0
cur_cut_cnt = 0
total_cut_cnt = 0

for cake in cakes:
    if cake == 10:
        answer += 1
    elif cake % 10 == 0 :
        heapq.heappush(ten_multi_cake, cake)
    else:
        heapq.heappush(not_ten_multi_cake, cake)

while ten_multi_cake:
    cake = heapq.heappop(ten_multi_cake)

    cur_cut_cnt = (cake // 10) -1

    if cur_cut_cnt > m - total_cut_cnt:
        answer += m - total_cut_cnt
        total_cut_cnt += m - total_cut_cnt
        break
    elif cur_cut_cnt == m - total_cut_cnt:
        answer += (cur_cut_cnt + 1)
        total_cut_cnt += cur_cut_cnt
        break
    else:
        answer += (cur_cut_cnt + 1)
        total_cut_cnt += cur_cut_cnt


if total_cut_cnt == m:
    print(answer)
elif total_cut_cnt < m:
    while not_ten_multi_cake:
        cake = heapq.heappop(not_ten_multi_cake)
        cur_cut_cnt = cake // 10

        if cur_cut_cnt > m - total_cut_cnt:
            answer += m - total_cut_cnt
            total_cut_cnt += m - total_cut_cnt
            break
        elif cur_cut_cnt == m - total_cut_cnt:
            answer += (cur_cut_cnt)
            total_cut_cnt += cur_cut_cnt
            break
        else:
            answer += cur_cut_cnt
            total_cut_cnt += cur_cut_cnt

    print(answer)
