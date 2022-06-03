import sys
sys.stdin = open('node_sum_input.txt')


T = int(input())

for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    # 초기 트리 구성하기
    tree_list = [[0, 0, 0] for _ in range(N + 1)]
    # [왼쪽노드, 값, 오른쪽노드] 형식으로 저장
    for i in range(1, (N + 1)//2):
        tree_list[i][0] = 2*i
        tree_list[i][2] = 2*i+1
        if not N % 2: #짝수일 경우 하나가 남아서 하나 더해주기
            tree_list[N//2][0] = N

    # 각각 노드 번호와 값을 가져와서 tree_list에 저장
    for _ in range(M):
        node, number = map(int, input().split())
        tree_list[node][1] = number

    # 제일 밑에 있는 자식 노드부터 차례대로 더해서 부모노드에 저장하기
    for i in range(N, 0, -1):
        # root까지
        if i // 2 > 0:
            tree_list[i // 2][1] += tree_list[i][1]

    # L번 노드 값 출력하기
    print(f'#{tc} {tree_list[L][1]}')






