import string

def solution(param0):
    answer = []

    fileList = []

    for paramElem in param0:
        paramList = paramElem.split("/") # 파일명 구하기 위해 /로 문자열 구분 리스트에 저장
        fileList.append(paramList[-1][0]+"."+paramList[-1][-1]) # 구분된 문자열을 저장한 리스트에서 마지막 인덱스가 파일명, 그리고 그 파일명에서 버전 정보 제외한 파일명 추출

    # file로만 구성된 리스트에서 같은 파일 값 찾기

    fileListSize = len(fileList)
    for i in range(fileListSize):
        cnt = 1
        for j in range(i+1,fileListSize):
            if fileList[i] == fileList[j]: #같은 파일명 찾으면 카운트값 1 증가
                cnt += 1
            
            if cnt != 1 and fileList[i] not in answer: # 동일한 파일명이 존재여부 및 중복 검사 
                answer.append(fileList[i])
                answer.append(str(cnt))

            