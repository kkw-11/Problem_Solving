def solution(tstring, variables):
    answer = ''

    tlist = tstring.split()
    vari_dict = {}

    for variable in variables:
        vari_dict[variable[0]] = [variable[1],False,None]
    
    for index, first_word in enumerate(tlist):
        value_word = first_word

        if value_word[0] == '{' and value_word[-1] == '}':
            if value_word[1:-1] in vari_dict:
                if vari_dict[value_word[1:-1]][1] == False:
                    while value_word[0] == '{' and value_word[-1] == '}':
                        if value_word[1:-1] in vari_dict:
                            value_word = vari_dict[value_word[1:-1]][0]
                            if value_word == first_word:
                                break
                        else:
                            break
                else:
                    value_word = vari_dict[value_word[1:-1]][2]

        tlist[index] = value_word
        if first_word[1:-1] in vari_dict and vari_dict[first_word[1:-1]][1] == False:
            vari_dict[first_word[1:-1]][2] = value_word
            vari_dict[first_word[1:-1]][1] = True

    answer = " ".join(tlist)
    return answer

tstring = "this is {template} {template} is {state}"
variables = [["template","{state}"], ["state","{templates}"]]

print(solution(tstring, variables))