def solution(boundary_column,boundary_row,rectangles):
    answer = []
    rectangle.sort()
    table = [[0]*boundary_column for _ in range(boundary_row)]

    for rectangle in rectangles:
        for _ in range(rectangle[1]):
            for row in range(boundary_row):
                find_where = False
                is_find =  False
                for col in range(boundary_column):
                    if table[row][col] == 0:
                        if col + rectangle[0] - 1 >= boundary_column or row + rectangle[0] - 1 >= boundary_row: continue #2차원 평면 범위 체크
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

boundary_column = 7
boundary_row = 8
rectangles = [[2,2],[1,4],[3,2]]
print(solution(boundary_column,boundary_row,rectangles))
