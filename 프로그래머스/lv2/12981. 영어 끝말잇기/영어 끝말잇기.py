def solution(n, words):
    # 가장 먼저 탈락하는 인덱스를 구하자
    find_index = 0
    for i in range(1, len(words)):
        if words[i] in words[:i]:
            find_index = i
            break
        if words[i - 1][-1] != words[i][0] :
            find_index = i
            break
    print(find_index)
    
    if find_index :
        answer = [find_index % n + 1, find_index//n + 1]
        
    else :
        answer = [0, 0]
    
    

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')

    return answer