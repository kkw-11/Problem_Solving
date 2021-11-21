#카카오 해커랭크 문제

def set_interval(a,b):
    a_to_b_set = []
    for i in range(len(a)):
        a_to_b_set.append((a[i],b[i]))
    a_to_b_set.sort()
    
    return a_to_b_set

def empty_interval(segment,k):
    res = []
    last = None
    if segment[0][0] != 1:
        res.append((1,1+k))
    last= segment[0][1]
    
    for idx, val in enumerate(segment[1:]):
        if val[0] <= last:
            if val[1] <= last:
                continue
            else:
                last = val[1]
        else:
            if idx != len(segment)-1 and last +k <= segment[idx+1][0]:
                res.append((last,last+k))
                last = val[1]
    return (last,res)
        
        
        
def minimumDivision(a, b, k):
    # Write your code here
    
    a_to_b_set = set_interval(a,b)
    temp = a_to_b_set[:]
    last,res=empty_interval(a_to_b_set,k)
    answer = []
    for elem in res:

        temp.append(elem)
        temp.sort()
        l,r = empty_interval(temp,k)
        answer.append(len(r)+1)
        
    return min(answer)


print(minimumDivision([ 2,13,27,45,45,33,] ,[ 10, 24, 40, 45,45,33 ]    ,12))