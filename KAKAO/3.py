from collections import defaultdict

def solution(fees, records):
    answer = []
    car_info = defaultdict(list)
    
    for record in records:
        value = record.split()
        car_info[value[1]].append(value[0])
    
    car_number= list(car_info.keys())
    car_number.sort()
    answer = [0]*len(car_number)
    # print(answer)
    for i in range(len(car_number)):
        if len(car_info[car_number[i]]) % 2 !=0:
            car_info[car_number[i]].append("23:59")
    
    # print(car_info)
    for i in range(len(car_number)):
        total_time = 0
        for j in range(0, len(car_info[car_number[i]]),2):
            # hour = car_info[car_number[i]][j+1].split(":")[0]
            # print(hour)
            # hour = car_info[car_number[i]][j].split(":")[0]
            # print(hour)
            
            hour = int(car_info[car_number[i]][j+1].split(":")[0]) - int(car_info[car_number[i]][j].split(":")[0])
            time = int(car_info[car_number[i]][j+1].split(":")[1]) - int(car_info[car_number[i]][j].split(":")[1])
            total_time += hour*60+time
            # print(hour*60+time)
        # print(total_time)
        if total_time <= fees[0]:
            answer[i] += fees[1]
        else:
            
            if (total_time-fees[0])%fees[2] != 0:
                overtime = int( (total_time-fees[0])/fees[2] +1)
            else:
                overtime = (total_time-fees[0])/fees[2]
                
            answer[i] = fees[1] + overtime * fees[3]
    print(answer)
    return answer