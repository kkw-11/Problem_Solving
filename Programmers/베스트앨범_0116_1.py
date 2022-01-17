def solution(genres, plays):
    def max_genre_func():
        max_val = 0
        max_genre = ""
        for key, val in best.items():
            if val[0] > max_val:
                max_genre = key
                max_val = val[0]
        return max_genre

    answer = []
    n = len(genres)
    best = {}

    for i in range(n):
        if not genres[i] in best:
            best[genres[i]] = [plays[i] ,[(plays[i],-i)]]
        else:
            best[genres[i]][0] += plays[i]
            best[genres[i]][1].append((plays[i],-i))
            
    while best:
        max_genre = max_genre_func()
    
        best[max_genre][1].sort(reverse = True)
        cnt = 0
        for a in best[max_genre][1]:
            cnt += 1
            answer.append(-a[1])
            if cnt >= 2:
                break
        del best[max_genre]

    return answer