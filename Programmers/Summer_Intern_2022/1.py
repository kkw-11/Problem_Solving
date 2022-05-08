def solution(atmos):
    answer = 0
    cnt = 0
    mask_flag = False
    day = 0
    for atom in atmos:
        dirty = ""
        micro = ""

        if atom[0] >= 81 or atom[1]>=36:
            if atom[0] >= 151 and atom[1]>=76:
                if mask_flag:
                    mask_flag = False
                    day = 0
                else:
                    cnt += 1
                    mask_flag = False
                    day = 0
            else:
                if mask_flag:
                    day += 1
                else:
                    mask_flag = True
                    cnt += 1
                    day = 1
        else:
            if mask_flag:
                day += 1

        if day >= 3:
            mask_flag = False
            day = 0

    return cnt