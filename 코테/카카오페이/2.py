def solution(n,m,rectangle):
    answer = []
    rectangle.sort()
    table = [[0]*n for _ in range(m)]

    for rec in rectangle:
        for _ in range(rec[1]):
                      
            for row in range(m):
                find_where = False
                not_find =  False
                for col in range(n):
                    if table[row][col] == 0:
                        if col + rec[0] - 1 >=n or row+rec[0]-1>=m: continue
                        for i in range(rec[0]):
                            if table[row][col+i] != 0:
                                not_find = True
                                break
                        if not_find:continue

                        find_where = True
                        break
                if find_where:
                    answer.append([col,row,rec[0]])
                    for i in range(rec[0]):
                        for j in range(rec[0]):
                            table[row+i][col+j] = rec[0]
                    break
    return answer

n = 7
m = 8
rectangle = [[2,2],[1,4],[3,2]]
print(solution(n,m,rectangle))
