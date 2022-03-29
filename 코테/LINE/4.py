
def solution(abilities, k):
    answer = 0
    gaps = []
    if len(abilities) % 2 == 1:
        abilities.append(0)
    abilities.sort(reverse=True)

    for i in range(0,len(abilities)-1,2):
        gaps.append((abilities[i]-abilities[i+1], abilities[i], abilities[i+1]))
    gaps.sort(reverse=True)

    for gap in gaps:
        if k>0:
            k -= 1
            answer += gap[1]
        else:
            answer += gap[2]

    return answer

abilities = [2, 8, 3, 6, 1, 9, 1, 9]
k = 2