
def solution(phone_book):
    check_dict = {}

    for phone_number in phone_book:
        check_dict[phone_number] = True
        
        #check_dict = ["123":True,"456":True,"789":True]

    for phone_number in phone_book: # phone_number "123"
        start_number = ""
        
        for number in phone_number: # number 1, 2,  3 
            start_number += number # "1" , "12", "123"

            if start_number != phone_number:
                if check_dict.get(start_number) != None: 
                    return False
    else:
        return True