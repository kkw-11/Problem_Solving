def solution(genres, plays):
    answer = []
    n = len(genres)
    best = {}

    for i in range(n):
        if not genres[i] in best:
            best[genres[i]] = [plays[i] ,[(plays[i],i)]]
        else:
            best[genres[i]][0] += plays[i]
            best[genres[i]][1].append((plays[i],i))

    best_value = sorted( list(best.values()), key= lambda x:-x[0] )
    print(best_value)

    for play_infos in best_value:
        play_info[1].sort(key=lambda x:(-x[0],x[1]))
        cnt = 0
        for play_info in play_infos[1]:
            cnt += 1
            answer.append(play_info[1])
            if cnt >= 2:
                break

    return answer