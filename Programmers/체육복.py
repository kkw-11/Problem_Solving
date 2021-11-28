def solution(n, lost, reserve):
    answer = 0
    students = [1]*(n+1)
    
    for l in lost:
        students[l] -= 1
    for r in reserve:
        students[r] += 1

        
    for student_number, number_of_clothes in enumerate(students):
        if number_of_clothes == 2 :
            if student_number != 1 and student_number != n:
                if students[student_number+1] == 0:
                    students[student_number] -= 1
                    students[student_number+1] += 1
                    continue
                    
                if students[student_number-1] == 0:
                    students[student_number] -= 1
                    students[student_number-1] += 1
            
            if student_number == 1:
                if students[student_number+1] == 0:
                    students[student_number] -= 1
                    students[student_number+1] += 1
            
            if student_number == n:
                if students[student_number-1] == 0:
                    students[student_number] -= 1
                    students[student_number-1] += 1
        print(students[1:])
    answer = n - students.count(0)
        
    return answer