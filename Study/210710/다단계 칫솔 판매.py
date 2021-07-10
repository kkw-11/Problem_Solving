# https://programmers.co.kr/learn/courses/30/lessons/77486


def solution(enroll, referral, seller, amount):
    
    tree = {'-' : 'root'}
    sell = {'-' : 0}

    for i in range(len(enroll)):
        child = enroll[i]
        parent = referral[i]
        sell[child] = 0
        tree[child] = parent

    for i in range(len(seller)):
        child = seller[i]
        parent = tree[child]
        money = amount[i] * 100
        sell[child] += money
        
        while True:
            commission = money // 10
            sell[child] -= commission
            sell[parent] += commission
            child = parent
            parent = tree[child]
            money = commission
            if parent == 'root':
                break
                
    ans = []
    for person in enroll:
        ans.append(sell[person])
    
    return ans