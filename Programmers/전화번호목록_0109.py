def solution(phone_book):
    n = len(phone_book)
    check_dict = {}

    for phone_number in phone_book:
        check_dict[phone_number] = True

    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number

            if temp != phone_number and temp in check_dict:
                return False
    else:
        return True