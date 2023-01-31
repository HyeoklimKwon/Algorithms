def solution(s):
    # def delete_alphas(alphabets):
    #     tmp_list = []
    #     i = 0
    #     while i < len(alphabets):
    #         if i == len(alphabets) - 1:
    #             tmp_list.append(i)
    #         else:
    #             if alphabets[i] == alphabets[i + 1]:                
    #                 i += 1
    #             else:
    #                 tmp_list.append(i)              
    #         i += 1
    #     if tmp_list:
    #         for i in range(len(tmp_list)):
    #             tmp_list[i] = alphabets[tmp_list[i]]
    #         return tmp_list
    #     else :
    #         return False
    # s = list(s)
    # answer = 1
    # while s:
    #     check_list = delete_alphas(s)
    #     if check_list == s:
    #         answer = 0
    #         break
    #     s = check_list  
    stack = []
    for letter in s:
        if stack:
            if stack[-1] == letter:
                stack.pop()
            else :
                stack.append(letter)
        else :
            stack.append(letter)
    if stack:
        answer = 0
    else :
        answer = 1
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.

    
    return answer