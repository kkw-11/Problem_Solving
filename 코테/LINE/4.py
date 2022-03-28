
def solution(abilities, k):
    answer = 0
    difs = []
    if len(abilities) % 2 == 1:
        abilities.append(0)
    abilities.sort(reverse=True)

    for i in range(0,len(abilities)-1,2):
        difs.append((abilities[i]-abilities[i+1],abilities[i],abilities[i+1]))
    difs.sort(reverse=True)

    for dif in difs:
        if k>0:
            k -= 1
            answer += dif[1]
        else:
            answer += dif[2]

    return answer

abilities = [2, 8, 3, 6, 1, 9, 1, 9]
k = 2