# sort lambda 사용
def solution(genres, plays):
    answer = []
    genres_cnt = {}

    for i in range(len(genres)):
        if genres[i] in genres_cnt:
            genres_cnt[genres[i]][0] += plays[i]
            genres_cnt[genres[i]][1].append((plays[i],i))

        else:
            genres_cnt[genres[i]] = [plays[i],[(plays[i],i)]]

    def max_genre():
        max_value = 0
        for key, value in genres_cnt.items():
            if value[0] > max_value:
                max_value = value[0]
                genre = key

        return genre

    for _ in range(len(genres_cnt)):
        genre = max_genre()
        genres_cnt[genre][1].sort(key=lambda x:(-x[0],x[1]))
        cnt = 0
        for a in genres_cnt[genre][1]:
            cnt += 1
            answer.append(a[1])
            if cnt >= 2:
                break
        del genres_cnt[genre]


    return answer