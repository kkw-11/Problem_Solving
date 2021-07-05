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
        musicLists[genres[i]].append([i,plays[i]])
        genresTotalPlays[genres[i]] += plays[i]
            
    while len(genresTotalPlays)>0:
        maxTotal = 0
        maxGenre = ""
        
        #최대 장르 구하기
        for genreKey, totalPlayVal in genresTotalPlays.items():
            if totalPlayVal > maxTotal:
                maxGenre = genreKey
                maxTotal = totalPlayVal

        for i in range(2):
            play = 0 
            musicNum = -1
            maxPlayidx = -1
            for musicListIdx, musicList in enumerate(musicLists[maxGenre]):
                if play < musicList[1]:
                    play = musicList[1]
                    musicNum = musicList[0]
                    maxPlayidx = musicListIdx
            else:
                if musicNum == -1:
                    break
                else:
                    answer.append(musicNum)
                    musicLists[maxGenre].pop(maxPlayidx)
        
        del genresTotalPlays[maxGenre]
                    
    
    return answer