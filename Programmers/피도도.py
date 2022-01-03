def solution(k, dungeons):
    visited = [False]*len(dungeons)
    
    answer = 0
    
    def go(reserved_HP,depth):
        nonlocal answer
        if depth > answer:
            answer = depth

        for dungeon_number in range(len(dungeons)):
            if dungeons[dungeon_number][0] <= reserved_HP and not visited[dungeon_number]:
                visited[dungeon_number] = True
                go(reserved_HP-dungeons[dungeon_number][1], depth+1)
                visited[dungeon_number] = False
    
    go(k, 0)
    
    return answer