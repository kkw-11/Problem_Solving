from collections import defaultdict
def solution(genres, plays):
    answer = []
    total = 0
    maxTotal = -1
    musicLists = defaultdict(list)
    genresTotalPlays = defaultdict(int)
    
    # genre: album[genre]
    # "classic" : [(0,500),(2,150),()]
    for i in range(len(genres)):
        musicLists[genres[i]].append((i,plays[i]))
        genresTotalPlays[genres[i]] += plays[i]
            
    while len(genresTotalPlays)>0:
        maxTotal = 0
        maxGenre = ""
        for genreKey, totalPlayVal in genresTotalPlays.items():
            if totalPlayVal > maxTotal:
                maxGenre = genreKey
                maxTotal = totalPlayVal
        else:
            del genresTotalPlays[maxGenre]
        

        for i in range(2):
            play = 0 
            musicNum = -1            
            for musicList in musicLists[maxGenre]:
                if musicList[1] < play:
                    play = musicList[1]
                    musicNum = musicList[0]
            else:
                if musicNum == -1:
                    break
                else:
                    answer.append(musicNum)
                    musicList.remove((musicNum,play))


    
    return answer