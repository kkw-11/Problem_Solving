# Plase note that external libraries, such as NumPy or Pandas
# are NOT available for this task

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


def solution(S):
    # write your code in Python 3.6
    file_dict = {}
    s_list= S.splitlines()
    answer = ""

    for file_info in s_list:
        file_info_list = file_info.split(",")
        if file_info_list[1] not in file_dict:
            file_dict[file_info_list[1]] = [[file_info_list[2], file_info_list[0]]]
        else:
            file_dict[file_info_list[1]].append([file_info_list[2],file_info_list[0]])

    for key in file_dict.keys():
        file_dict[key].sort(key=lambda x:x[0])

    for key in file_dict.keys():
        digit = len(str(len(file_dict[key])))
        
        for index, value in enumerate(file_dict[key]):
            value_list = value[1].split(".")
            file_dict[key][index].append( key + str(index+1).zfill(digit) + "." + value_list[1])
            

    for file_info in s_list:
        file_info_list = file_info.split(",")

        for value in file_dict[file_info_list[1]]:
            if value[1] == file_info_list[0]:
                answer += value[2].strip()
                answer += "\n"
            


    return answer

