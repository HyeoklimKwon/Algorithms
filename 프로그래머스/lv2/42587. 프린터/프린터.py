from collections import deque
def solution(priorities, location):
#     1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
#     2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
#     3. 그렇지 않으면 J를 인쇄합니다.
    q = deque()
    for i in range(len(priorities)):
        q.append([i, priorities[i]])
    cnt = 0
    while q :
        index, nowp = q.popleft()
        flag = True
        for i in range(len(q)):
            if nowp < q[i][1]:
                q.append([index,nowp])
                flag = False
                break
        if flag:
            cnt += 1            
            if index == location :
                break
  
        
    
    answer = cnt
    
    return answer