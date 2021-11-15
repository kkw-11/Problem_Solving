while True:
    try:
        where = list(map(int,input().split()))
        where.sort()

        max_distance =  max(where[2]-where[1],where[1]-where[0])
        print(max_distance-1)
    except:
        break
