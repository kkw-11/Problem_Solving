import re
def solution(call):
    answer = ""
    temp = []
    call_lower = call.lower()

    pattern = "[a-z]{1}"
    letters = set(re.findall(pattern,call_lower))


    for letter in letters:
        temp.append((call_lower.count(letter),letter))
    temp.sort(reverse=True)

    max_cnt = temp[0][0]

    for cnt, ch in temp:
        if cnt  < max_cnt:
            break
        call = call.replace(chr(ord(ch)-32),"")
        call = call.replace(ch,"")

    return call

call = "abcabcdefabc"
print(solution(call))
