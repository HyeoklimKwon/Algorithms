from collections import deque
def solution(s):
    # 2. 회전시킨 괄호 검사하기
    open_stack = []
    open_garo = ['[', '{', '(']
    close_garo = [']', '}', ')']   
    def check(garos) :
        for garo in garos:
            if garo in open_garo:
                open_stack.append(garo)
            else:
                if open_stack:
                    tmp_garo = open_stack.pop()                    
                    if open_garo[close_garo.index(garo)] != tmp_garo:
                        return False
                else :
                    return False
        if open_stack:
            return False
        else :
            return True
    
    # 1. 괄호 회전시키기 
    cnt = 0
    s = list(s)
    q = deque(s)
    # print(check(")[{}]("))
    # index = 0
    # while cnt < len(s): 
          
        
    for _ in range(len(s)):
        if check(q):
            cnt += 1       
        tmp_letter = q.popleft()
        q.append(tmp_letter)        
    
    answer = cnt
    return answer