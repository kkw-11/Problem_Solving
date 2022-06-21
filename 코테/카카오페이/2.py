def solution(n,m,rectangles):
    answer = []
    rectangle.sort()
    table = [[0]*n for _ in range(m)]

    for rectangle in rectangles:
        for _ in range(rectangle[1]):
            for row in range(m):
                find_where = False
                is_find =  False
                for col in range(n):
                    if table[row][col] == 0:
                        if col + rectangle[0] - 1 >= n or row + rectangle[0] - 1 >= m: continue #2차원 평면 범위 체크
                        for i in range(rectangle[0]):
                            if table[row][col+i] != 0:
                                is_find = True
                                break
                        if is_find:continue
                        find_where = True
                        break
                if find_where:
                    answer.append([col,row,rectangle[0]])
                    for i in range(rectangle[0]):
                        for j in range(rectangle[0]):
                            table[row+i][col+j] = rectangle[0]
                    break
                
    return answer

n = 7
m = 8
rectangles = [[2,2],[1,4],[3,2]]
print(solution(n,m,rectangles))
