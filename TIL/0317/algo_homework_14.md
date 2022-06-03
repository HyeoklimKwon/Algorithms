```python
T = 10

for tc in range(1, T + 1):
    N = int(input())
    tree_list = [[0, 0, 0] for _ in range(N + 1)]
    # [ 값,왼쪽노드 ,오른쪽노드] 형식으로 저장
    input_list = [list(map(str, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(len(input_list[i])-1):
            tree_list[i+1][j] = input_list[i][j+1]

	#완전 이진트리가 아니기 때문에 부모노드로부터 재귀함수 생성
    def rec(n):
        global tree_list
        #부호일 경우 다시 함수에 자식노드를 넣고 그 결과값을 부호로 계산
        if tree_list[n][0] == '-':
            tree_list[n][0] = rec(int(tree_list[n][1])) - 
            rec(int(tree_list[n][2]))
        elif tree_list[n][0] == '*':
            tree_list[n][0] = rec(int(tree_list[n][1])) * 
            rec(int(tree_list[n][2]))
        elif tree_list[n][0] == '+':
            tree_list[n][0] = rec(int(tree_list[n][1])) + 
            rec(int(tree_list[n][2]))
        elif tree_list[n][0] == '/':
            tree_list[n][0] = rec(int(tree_list[n][1])) /
            rec(int(tree_list[n][2]))
        # 값일 경우에는 그대로 호출
        else:
            tree_list[n][0] = int(tree_list[n][0])
		# 결과값 출력
        return tree_list[n][0]
	#최종값이기 때문에 rec(1)을 출력한다.
    print(f'#{tc} {int(rec(1))}')
```

