# c언어와 다르게 전역 변수로 선언된 변수명과 똑같은 변수를 함수내에서 사용하게 되면 지역변수로 인식한다
# print()는 자료를 우리에게 보여주는 역할을 하고, return은 함수의 명령 결과를 함수 밖으로 전달해주는 역할을 한답니다. :) 
# 함수내부에서 일이 외부에 영향을 미치지 못한다.

# 다음은 표준어로 "밥 먹었어요?"가 담긴 변수 greeting입니다.
greeting = "밥 먹었어요?"

# 이를 print로 출력하면 다음과 같습니다.
print("서울 :",greeting)

# 함수 busan을 선언하고, 그 안에 변수 greeting에 "밥 뭇나?"를 넣어봅시다.
def busan():
    greeting = "밥 뭇나?"   #C언어와 다르게 greeting을 위에서 전역변수로 선언하였지만 지역변수로서 동작한다. 
    print("부산 :",greeting)
# 함수 busan을 실행해보세요.
busan()

# 변수 greeting을 출력해보세요.
print(greeting)

