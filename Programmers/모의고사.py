def solution(answers):
    answer = []
    n = len(answers)
    student1_answer = [1, 2, 3, 4, 5]
    student2_answer = [2, 1, 2, 3, 2, 4, 2, 5]
    student3_answer = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    len_student1_answer = len(student1_answer)
    len_student2_answer = len(student2_answer)
    len_student3_answer = len(student3_answer)
    
    count1 = 0
    count2 = 0
    count3 = 0

    for question_number in range(len(answers)):
        if answers[question_number] == student1_answer[question_number%len_student1_answer]:
            count1 += 1
        if answers[question_number] == student2_answer[question_number%len_student2_answer]:
            count2 += 1
        if answers[question_number] == student3_answer[question_number%len_student3_answer]:
            count3 += 1
    
    answer_count = [count1, count2, count3]
    max_answer_count = max(answer_count)
    for person, score in enumerate(answer_count):
        if score == max_answer_count:
            answer.append(person+1)
                
    return answer