def solution(n, t, m, p):
    
    def change_binary(number):
        result = ''
        if number == 0 :
            return str(0)
        while number >= n:
            result = str(number % n) + result
            number //= n            
        result = str(number % n) + result
        return result
    
    def turn_alphabet(number):
        alphabets = ['A', 'B', 'C', 'D', 'E', 'F']
        if 10 <= number < n :
            return alphabets[number % 10]        
        if number >= 10:
            number %= 10
            return alphabets[number]
        else :
            return number
    
    def change_heximal(number):
        result = ''
        if number < n :
            return str(turn_alphabet(number))
        while number >= n:
            result = str(turn_alphabet(number % n)) + result
            number //= n
            # print(number)
        result = str(turn_alphabet(number % n)) + result
        return result
    
    cnt = 0
    now_num = []
    result = ''
    if n <= 10:
        # print(change_binary(39))
        num_cnt = 0
        while cnt < t :
            cnt += 1
            
            # print(len(now_num))
            while len(now_num) < p :                
                now_num.extend(list(change_binary(num_cnt)))
                num_cnt += 1
                if len(now_num) >= p:
                    break
                    
            # print(now_num)
            result += now_num[p - 1]
            p += m
    else :
        num_cnt = 0
        while cnt < t :
            cnt += 1
            
            # print(len(now_num))
            while len(now_num) < p :
                # print(num_cnt)
                # print(change_heximal(num_cnt))
                
                now_num.extend(list(change_heximal(num_cnt)))
                num_cnt += 1
                # if len(now_num) >= p:
                #     break
                # print(now_num)    
            # print(now_num)
            result += now_num[p - 1]
            p += m
            
#         # print(change_heximal(130))
#     print(result)    
    # print(change_heximal(299))
    # print(change_heximal(711))
    answer = result
    return answer