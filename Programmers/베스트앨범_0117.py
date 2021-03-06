def solution(genres, plays):
    answer = []
    best = {}

    for song_number, genre in enumerate(genres):
        if not genre in best:
            best[genre] = [plays[song_number], [(plays[song_number], song_number)]]
        else:
            best[genre][0] += plays[song_number]
            best[genre][1].append((plays[song_number], song_number))
            
    best_genres_sort = sorted(best.values(), key=lambda x:-x[0])

    for genre_play_info in best_genres_sort:
        rank_song = [i[1] for i in sorted(genre_play_info[1],key = lambda x:(-x[0],x[1]))][:2]
        answer.extend(rank_song)

    return answer