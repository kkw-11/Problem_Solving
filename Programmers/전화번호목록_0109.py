def solution(phone_book):
    n = len(phone_book)
    check_dict = {}

    for phone_number in phone_book:
        if not phone_number in check_dict:
            check_dict[phone_number] = True

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number

            if len(temp) != len(phone_number):
                if not temp in check_dict:
                    pass
                elif check_dict[temp]:
                    return False
    else:
        return Truet