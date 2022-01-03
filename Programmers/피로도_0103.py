from itertools import permutations
def solution(k, dungeons):
    answer = 0
    permutation = permutations(dungeons)

    for dungeon_seq in permutation: #[80, 20], [50, 40], [30, 10]
        cnt = 0
        temp = k
        for dungeon_each in dungeon_seq:
            if dungeon_each[0] <= temp:
                temp -= dungeon_each[1]
                cnt += 1
            else:
                break
        
        if cnt > answer:
            answer = cnt
            if answer == len(dungeons):
                break

    return answer