def solution(genres, plays):
    answer = []
    best = {}

    for index, genre in enumerate(genres):
        if not genre in best:
            best[genre] = [plays[index],[(plays[index], index)]]
        else:
            best[genre][0] += plays[index]
            best[genre][1].append((plays[index], index))
    best_genres_sort = sorted(best.values(), key=lambda x:-x[0])

    for genre_play_info in best_genres_sort:
        rank_song = [i[1] for i in sorted(genre_play_info[1],key = lambda x:(-x[0],x[1]))][:2]
        answer.extend(rank_song)

    return answer