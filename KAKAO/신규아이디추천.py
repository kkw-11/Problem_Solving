import re
def solution(new_id):
    answer = ''
    answer = new_id.lower()

    answer = re.sub('[^a-z\d\-\_\.]','',answer)

    answer = re.sub('\.\.+','.',answer)
    answer = re.sub('^\.|\.$','',answer)
    if answer == '':
        answer = 'a'
    if len(answer) >= 16:
        answer = answer[:15]
    answer = re.sub('^\.|\.$','',answer)

    while len(answer) <= 2:
        answer = answer + answer[-1:]

    return answer