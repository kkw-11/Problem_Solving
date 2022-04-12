def solution(path):
    answer = []
    where_dir = ["N","E","S","E"]

    cur = 0

    while cur < len(path):
        for next in range(cur+1,len(path)):
            if path[cur] == path[next]:
                continue
            else:
                if next >= cur+6:
                    break
                index_dif = path.index(path[cur]) - path.index(path[next])
                x = cur
                y = (next-cur)*100
                dir = "right" if index_dif == 1 or index_dif == 3 else "left"

                temp = f"Time {cur}:Go straight {y}m {dir}"
                answer.append(temp)
                cur = next - 1
        cur += 1

    return answer

path = "EEESEEEEEENNNN"
print(solution(path))
