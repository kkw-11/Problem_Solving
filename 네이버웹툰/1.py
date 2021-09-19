def solution(N,money,T,K):
    answer = 0
    atm = [0]*N

    def input_money(atm_number):
        if atm_number == N:
            if sum(atm) == money:
                for i in range(N-T):
			        if sum(atm[i:i+T]) > K:
                        break
                else:
                    answer += 1
        
        for my_money in range(money-sum(atm[:atm_number])):
            atm[atm_number] = my_money
            input_money(atm_number+1)
    
    for my_money in range(K+1):
        atm[0] = my_money
        input_money(1)

    return answer



