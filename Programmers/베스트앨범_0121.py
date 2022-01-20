def solution(genres, plays):
    answer = []
    best = {}
    
    for song_number, genre in enumerate(genres):
        if not genre in best:
            best[genre] = [plays[song_number], [(song_number,plays[song_number])] ]
        else:
            best[genre][0] += plays[song_number]
            best[genre][1].append((song_number,plays[song_number]))
        
    best_values_sort = sorted(best.values(), key=lambda x:-x[0])
    
    for plays_infos in best_values_sort:
        answer.extend([play_info[0] for play_info in sorted(plays_infos[1],key=lambda x:(-x[1],x[0]))[:2]])
                          
    return answer