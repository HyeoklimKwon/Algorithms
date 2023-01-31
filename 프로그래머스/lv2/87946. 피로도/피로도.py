def solution(k, dungeons):
    visited = [0]*len(dungeons)
    global max_cnt
    max_cnt = 0   
    def check(visited, k):
        for i in range(len(visited)):
            if not visited[i]:
                if k >= dungeons[i][0]:
                    return True
        return False
                
    def dfs(k, visited, cnt):
        global max_cnt
        # 모두 방문했을 경우,
        if sum(visited) == len(dungeons):
                if max_cnt < cnt:
                    max_cnt = cnt
                    return
        # 남은 피로도로 갈 수 잇는 던전 체크 
        if not check(visited, k):
            if max_cnt < cnt:
                    max_cnt = cnt
                    return           
        
        # 모두 방문하지 않았을 경우, 순회하면서 방문하지 않은 곳
        for i in range(len(dungeons)):                        
            if not visited[i]:              
                if k >= dungeons[i][0]:
                    k -= dungeons[i][1]
                    cnt += 1
                    visited[i] = 1
                    # print(visited)
                    dfs(k, visited, cnt)
                    k += dungeons[i][1]
                    cnt -= 1
                    visited[i] = 0 
                    
    dfs(k, visited, 0) 
    # print(max_cnt)
    # print(visited)
     
    answer = max_cnt
    return answer