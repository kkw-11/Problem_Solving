import string

def solution(n, k):
    answer = 0


    tmp = string.digits+string.ascii_lowercase
    def convert(num, base) :
        q, r = divmod(num, base)
        if q == 0 :
            return tmp[r] 
        else :
            return convert(q, base) + tmp[r]
        
    convert_number = convert(n,k)
    
    #에라토스테네스의 체
    def is_prime_num(n):
        if n == 1:
            return False
        ch = [0]*(n+1)

        for i in range(2,n+1):
            if ch[i] == 0:
                for j in range(i+i,n+1,+i):
                    ch[j] = 1
        else:
            if ch[n]:
                return False
            else:
                return True
    
    len_number = len(convert_number)
    
    if '0' not in convert_number and is_prime_num(int(convert_number)):
        answer+=1
    
    # 0P0
    for start, digit in enumerate(convert_number):
        if digit == '0' :
            for end in range(start+1,len_number):
                if convert_number[end] == '0':
                    # print(int(convert_number[start+1:end]))
                    if '0' not in convert_number[start+1:end]:
                        if is_prime_num(int(convert_number[start:end].split()[0])):
                            print(int(convert_number[start+1:end]))
                            answer += 1
                            break
    # P0
    for index, digit in enumerate(convert_number):
        if digit == '0':
            if is_prime_num(int(convert_number[:index])):
                answer += 1
                break
        
    # 0P
    for index in range(len(convert_number)-1,-1,-1):
        if convert_number[index] == '0':
            if is_prime_num(int(convert_number[index+1:])):
                answer += 1
                break
            
    return answer