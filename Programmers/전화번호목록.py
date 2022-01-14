def solution(phone_book):
    check_dict = {}


    for phone_number in phone_book: 
        check_dict[hash(phone_number)] = phone_number
 
 
    for phone_number in phone_book:
        
        start_number = ""
        for number in phone_number:
            start_number = start_number + number

            if start_number != phone_number and hash(start_number) in check_dict:
                return False
    else:
        return True