def solution(storey):
    answer = 0
    while storey != 0 :
        #앞자리 검사를 위해 
        n = storey % 10
        k = storey + 10 - n
        k %= 100       
        if n >= 6 :
            answer += 10 - n
            storey += 10 - n
        # 앞자리가 6 이상일 경우 
        elif n == 5 and (storey // 10) % 10 >= 5:
            answer += 10 - n
            storey += 10 - n
        else :
            storey -= n
            answer += n
        storey //= 10
    return answer