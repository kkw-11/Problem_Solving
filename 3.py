def solution(money, costs):
   answer = 0
   coins = [1, 5, 10, 50, 100, 500]
   unit_cost = []

   for i in range(6):
       unit_cost.append((coins[i]/costs[i],costs[i],coins[i]))

   unit_cost.sort(reverse=True)
   index = 0 

   for index in range(6):
       answer += (money//unit_cost[index][2])*unit_cost[index][1]
       money -= (money//unit_cost[index][2])*unit_cost[index][2]

       if money == 0:
           break

   return answer

def factorial(n):
   result = 1
   for item in range(1, n+1, 1): 
       result *= item
   return result

def solution(width, height, diagonals):
    answer = 0

    for diagonal in diagonals:
        first_point = [diagonal[0]-1,diagonal[1]]

        first_route = factorial(sum(first_point))//((factorial(first_point[0])*factorial(first_point[1])))
        second_route = factorial(sum([width-first_point[0],height-first_point[1]]))//(factorial(width-first_point[0])*factorial(height-first_point[1]))
        answer += first_route*second_route

        second_point = [diagonal[0],diagonal[1]-1]
        
        first_route = factorial(sum(second_point))//((factorial(second_point[0])*factorial(second_point[1])))
        second_route = factorial(sum([width-second_point[0],height-second_point[1]]))//(factorial(width-second_point[0])*factorial(height-second_point[1]))
        answer += first_route*second_route

    answer = answer % 10000019

    return answer