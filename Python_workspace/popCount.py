# list에서 특정 원소의 개수를 세는 함수 -> list.count(3) //리스트에서 3이라는 원소의 개수를 반환
# list에서 특정 인덱스의 원소를 제거하는 함수 -> list.pop(0) // 리스트에서 인덱스 0번, 즉 첫 번째 인덱스의 원소를 제거한다
# list에서 특정 원소를 찾아 제거하는 함수 list.remove(2) // 리스트에서 '2'라는 원소를 찾아 제거 이때 '2'라는 원소가 여러개일 경우 가장 앞쪽의 '2'를 제거


my_list = [1,2,2,3,3,3]
var1 = my_list.count(3)
my_list.pop(0)
my_list.pop()
my_list.pop()
my_list.remove(2)
print(my_list)