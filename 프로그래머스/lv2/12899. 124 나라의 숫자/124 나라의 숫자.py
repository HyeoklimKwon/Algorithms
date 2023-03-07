def solution(n):
    number = int(n)
    result = []
    while True:
        remain = number % 3
        if remain == 0 :
            remain = 4
            number //= 3
            number -= 1
        else:
            number //= 3
        result.insert(0, remain)
        
        if number == 0 :
            break
    
    answer = ''
    for number in result:
        answer += str(number)
    return answer