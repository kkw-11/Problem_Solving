# https://moondol-ai.tistory.com/294
# https://moondol-ai.tistory.com/294

def solution(genres, plays):
    answer = []
    best = {}
    for i, genre in enumerate(genres):
        if genre in best.keys():
            best[genre][0] += plays[i]
            best[genre][1].append((i, plays[i]))
        else:
            best[genre] = [plays[i], [(i, plays[i])]]

    best = sorted(best.values(), reverse = True)
    for song in best:

        #a = [i[0] for i in sorted(song[1], key=lambda x: (-x[1],x[0]))]
        
        a = []
        for i in sorted(song[1], key=lambda x: (-x[1],x[0])):
            a.append(i[0])

            b = a[:min(2, len(song))]
        answer.extend(b)
    return answer