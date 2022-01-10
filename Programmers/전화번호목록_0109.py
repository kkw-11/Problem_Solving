def solution(phone_book):
    n = len(phone_book)
    check_dict = {}

    for phone_number in phone_book:
        if not phone_number in check_dict:
            check_dict[phone_number] = True

    for phone_number in phone_book:
        start_number = ""
        for number in phone_number:
            start_number += number

            if len(start_number) != len(phone_number):
                if not start_number in check_dict:
                    pass
                elif check_dict[start_number]:
                    return False
    else:
        return True