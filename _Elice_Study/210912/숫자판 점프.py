import sys 
dir_col = [1,0,-1,0]
dir_row = [0,1,0,-1]
res = 0
answer = set()
def go(graph, row, col, depth):
    global res
    global answer
    if depth == 6:
        res = res * 10 + graph[row][col]
        answer.add(res)
        return
    else:
        res = res * 10 + graph[row][col]
        for dir in range(4):
            nr = row + dir_row[dir]
            nc = col + dir_col[dir]

            if nr>=0 and nr < 5 and nc>=0 and nc <5:
                go(graph,nr,nc,depth+1)
                res = res//10

if __name__ == "__main__":
    
    graph = []
    
    for i in range(5):
        input_data = list(map(int, sys.stdin.readline().rstrip().split()))
        graph.append(input_data)

    for row in range(5):
        for col in range(5):
            res =  0
            go(graph,row,col,1)

    print(len(answer))
