def solution(genres,plays ):
    answer = []
    genres_plays = {}

    for song_number, genre in enumerate(genres):
        if genre not in genres_plays:
            genres_plays[genre] = [plays[song_number],[(plays[song_number],song_number)]]
        else:
            genres_plays[genre][0] += plays[song_number]
            genres_plays[genre][1].append((plays[song_number],song_number))
    print(genres_plays)

    genres_plays_values = sorted(genres_plays.values(), key=lambda x:-x[0])
    print(genres_plays_values)

    '''
    {'classic': [1450, [(500, 0), (150, 2), (800, 3)]], 
      'pop'   : [3100, [(600, 1), (2500, 4)]]}
    [  [3100, [(600, 1), (2500, 4)]]  , [1450, [(500, 0), (150, 2), (800, 3)]]]
    '''
    for genres_plays_value in genres_plays_values:
        answer.extend( [play_info[1] for play_info in sorted(genres_plays_value[1],key=lambda x:(-x[0],x[1]))[:2] ] )

    return answer