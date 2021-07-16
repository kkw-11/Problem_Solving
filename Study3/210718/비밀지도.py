#https://techbook11.tistory.com/339

def tenTobinary(number):
    binary = []
    temp = number

    while temp:
        binary.insert(0, temp % 2)

        temp //= 2

    res = "".join(map(str,binary))
    return res


def solution(n, arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        binary1 = tenTobinary(arr1[i])
        binary2 = tenTobinary(arr2[i])

        while len(binary1) < n :
            binary1 = "0" + binary1

        while len(binary2) < n :
            binary2 = "0" + binary2

        secretMap = ""

        for j in range(n):
            if binary1[j] == "0" and binary2[j] == "0":
                secretMap += " "
            else:
                secretMap += "#"
        else:
            answer.append(secretMap)


    return answer