import sys
sys.stdin = open('binary_heap_input.txt')


def insert_tree(n):
    global tree_list
    for i in range(1, N+1):
        if not tree_list[i]:
            #빈자리이면
            tree_list[i] = n
            # 바꿔주기
            while tree_list[i//2] > tree_list[i] and i//2 != 0:
                tree_list[i], tree_list[i//2] = tree_list[i//2], tree_list[i]
                i = i//2
            break


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    #숫자 리스트 받아오기
    number_list = list(map(int, input().split()))
    # 초기 트리 구성
    tree_list = [0]*(N + 1)

    # 만든 함수를 이용하여 차례대로 tree_list에 삽입
    for i in number_list:
        insert_tree(i)

    result = 0
    #root에 도달할때까지 부모노드 더하기
    while N//2 != 0:
        result += tree_list[N//2]
        N = N//2
    print(f'#{tc} {result}')
