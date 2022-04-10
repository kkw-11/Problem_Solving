def solution(tstring, variables):
    answer = ''
    vari_dict = {}

    for variable in variables:
        vari_dict[variable[0]] = variable[1]

    tlist = tstring.split() # []
    for index, value in enumerate(tlist):
        temp = value #{template}

        while value[0] == "{" and value[-1] == "}": 
            if value[1:-1] in vari_dict:
                value = vari_dict[value[1:-1]]
                tlist[index] = value
                if temp == value: #무한반복
                    break
            else:
                break
        else:
            if value[0] == "{" and value[-1] == "}":
                tlist[index] = temp[1:-1]

    answer = " ".join(tlist)

    return answer






# import re
# def soution(call):
#     answer = ''
#     pattern_dict = {}
#     a = call.lower()
#     for i in range(1,len(call)):
#         pattern = "[A-z]{" + f"{i}" +"}" [A-z]{}
#         letters = re.findall(pattern, a)
#         for letter in letters:
#             pattern_dict 

#             # [(a,3),(b,3),(ab,1)]

#     .replace()                  











# def where_dir(start,next):
#     if start == "N":
#         if next == "E":
#             return "right"

#     return 


# def solution(path):
#     i = 0
#     answer = []
#     messages = []
#     while i < len(path):
#         for j in range(i,len(path)):
#             if path[i] == path[j]:
#                 continue
#             else:
#                 if j >= i+6:
#                     break
#                 else:
#                     direction = where_dir(path[i],path[j]])
#                     messages.append((str(i),str(j-i)*100,direction))
#                     i = j - 1
#                     break
#         i +=1

#     for x,y,direction in messages:
#         answer.append(f"Tiem {x}: Go straight{y}m and turn {direction}")

#     return answer