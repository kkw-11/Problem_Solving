def solution(periods, payments, estimates):
    answer = [0,0]

    VIP = False
    n = len(periods)

    for i in range(n):
        # i 회원의 이번달 VIP 여부 체크
        if periods[i] >= 60:
            if sum(payments[i]) >= 600000:
                VIP = True
        elif periods[i] >= 24:
            if sum(payments[i]) >= 900000:
                VIP = True            

        # 다음달 VIP 여부 체크
        if VIP == False:
            if periods[i] + 1 >= 60:
                if sum(payments[i][1:]) + estimates[i] >= 600000:
                    answer[0] += 1
            elif periods[i] + 1 >= 24:
                if sum(payments[i][1:]) + estimates[i] >= 900000:
                    answer[0] += 1
        else:
            if periods[i] + 1 >= 60:
                if sum(payments[i][1:]) + estimates[i] < 600000:
                    answer[1] += 1
            elif periods[i] + 1 >= 24:
                if sum(payments[i][1:]) + estimates[i] < 900000:
                    answer[1] += 1


    return answer