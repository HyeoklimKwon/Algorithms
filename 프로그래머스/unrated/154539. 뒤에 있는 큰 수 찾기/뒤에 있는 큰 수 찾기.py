from heapq import *
def solution(numbers):
    # answer = []
    # for i in range(len(numbers)):
    #     flag = True
    #     for j in range(i + 1, len(numbers)):           
    #         if numbers[i] < numbers[j]:
    #             answer.append(numbers[j])
    #             flag = False
    #             break
    #     if flag:
    #         answer.append(-1)
    
    n = len(numbers)
    answer = [-1] * n

    h = []

    for i in range(n):
        value = numbers[i]

        while h and h[0][0] < value:
            _, idx = heappop(h)
            answer[idx] = value

        heappush(h, [value, i])
    
    return answer