import re

def solution(dartResult):
    answer = 0
    exponent={'S':1, 'D':2, 'T':3}
    symbol={'*':2, '#':-1}
    cal=[None]*3
    attempts=re.findall(r"\d{1,2}[S,D,T][*,#]?",dartResult)
    for i in range(3):
        info = list(filter(None,re.findall("\d{1,2}|[S,D,T]|[*,#]?", attempts[i])))
        temp=int(info[0])**exponent[info[1]]
        if len(info)==3:
            temp*=int(symbol[info[2]])
            if i>0 and info[2]=='*':
                cal[i-1]*=int(symbol[info[2]])
        cal[i]=temp
    return sum(cal)