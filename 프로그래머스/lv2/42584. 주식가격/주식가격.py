def solution(prices):
    
    stack = []
    result = [0] * len(prices)
    for i in range(len(prices)):
        # stack이 있을 경우
        if stack:
            while stack and stack[-1][0] > prices[i]:
                price, index = stack.pop()
                result[index] = i - index
            stack.append([prices[i], i])
        # 스택이 비었을 경우 추가
        else :
            stack.append([prices[i], i]) 
    for s in stack:
        price, index = s
        result[index] = len(prices) - 1 - index
    # print(result)
    answer = result
    return answer