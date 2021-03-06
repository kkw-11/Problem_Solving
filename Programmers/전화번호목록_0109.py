def solution(phone_book):
    check_dict = {}

    for phone_number in phone_book:
        check_dict[phone_number] = True

    for phone_number in phone_book:
        start_number = ""
        for number in phone_number:
            start_number += number

            if len(start_number) != len(phone_number):
                if start_number in check_dict:
                    return False
    else:
        return True
        