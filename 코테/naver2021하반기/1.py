
def solution(cards):
    answer = 0
    people = len(cards)
    checked = [False]*people #교환여부
    min_card_info = [] #(최소 카드 수(점수), 인덱스)
        
    
# 30
# 최소값 찾기
    for person in range(people):
        min_card = 999
        for card,index in enumerate(cards[person]):
            if card < min_card:
                min_card_info.append((card,index))


# 1번부터 다음사람 카드비교하면서 교환하고 아니면 원래로 되돌리기(반복문으로)
    for person1 in range(people-1): #1,2,3,
        if checked[person1]:
            continue
        for person2 in range(1,people):
            # 교환했으면 패스
            if checked[person2]:
                continue
            
            #[0,0,30]
            #[0,0,30]

            # 교환전
            # [8,8,14] [(8,0)]
            # [8,7,15] [(7,1)]

            # 교환후            
            # [9,7,14] [(8,0)]
            # [7,8,15] [(7,1)]
            
            
            # 같은 위치일때 교환안하는 코드
            # 둘다 이득이 되는지 여부 체크해서 교환하고 아니면 되돌리기 (0카드가 최소일때는 교환안하기 )
            if min_card_info[person1][1] != min_card_info[person2]:
                cards[person1][min_card_info[person1][1]] += 1
                cards[person2][min_card_info[person1][1]] -= 1

                cards[person2][min_card_info[person2][1]] += 1
                cards[person1][min_card_info[person2][1]] += 1

            # 다른위치일때 교환했는데 이득안되는 경우, 최소값이 안바뀜
            # 되돌리기


# 최종 카드 결과 최소값 찾아서 더해서 반환