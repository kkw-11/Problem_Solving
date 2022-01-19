def solution(genres, plays):
    answer = []
    best = {}

    for song_number, genre in enumerate(genres):
        if not genre in best:
            best[genre] = [plays[song_number], [(song_number, plays[song_number])]]
        else:
            best[genre][0] += plays[song_number]
            best[genre][1].append((song_number, plays[song_number]))
            
    for genre_play_info in sorted(best.values(), key=lambda x:-x[0]):
        
        answer.extend([play_info[0] for play_info in sorted(genre_play_info[1], key = lambda x:(-x[1],x[0]))[:2]])
           
    return answer