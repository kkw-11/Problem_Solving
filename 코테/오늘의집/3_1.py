def solution(tstring, variables):
    answer = ''

    tlist = tstring.split()
    template_dict = {}

    for variable in variables:
        template_dict[variable[0]] = [variable[1],False,None]
    print(template_dict)
    for index, word in enumerate(tlist):
        temp = word
        if word[0] == '{' and word[-1] == '}':
            if word[1:-1] not in template_dict:
                continue
            else:
                if template_dict[word[1:-1]][1]:
                    tlist[index] = template_dict[word[1:-1]][2]
                else:
                    while word[0] == '{' and word[-1] == '}':
                        if word[1:-1] in template_dict:
                            word = template_dict[word[1:-1]][0]
                        else:
                            break

                        if temp == word:
                            break
                    
                    tlist[index] = word
                    template_dict[temp[1:-1]][1] = True
                    template_dict[temp[1:-1]][2] = word


    answer = " ".join(tlist)
    return answer

tstring = "this is {template} {state}"
variables = [['template','{state}'],['state','{template}']]

print(solution(tstring, variables))