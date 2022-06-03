import sys
sys.stdin = open('tree_calc_input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    tree_list = [[0, 0, 0] for _ in range(N + 1)]
    # [ 값,왼쪽노드 ,오른쪽노드] 형식으로 저장
    input_list = [list(map(str, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(len(input_list[i])-1):
            tree_list[i+1][j] = input_list[i][j+1]


    def rec(n):
        global tree_list
        if tree_list[n][0] == '-':
            tree_list[n][0] = rec(int(tree_list[n][1])) - rec(int(tree_list[n][2]))
        elif tree_list[n][0] == '*':
            tree_list[n][0] = rec(int(tree_list[n][1])) * rec(int(tree_list[n][2]))
        elif tree_list[n][0] == '+':
            tree_list[n][0] = rec(int(tree_list[n][1])) + rec(int(tree_list[n][2]))
        elif tree_list[n][0] == '/':
            tree_list[n][0] = rec(int(tree_list[n][1])) / rec(int(tree_list[n][2]))
        else:
            tree_list[n][0] = int(tree_list[n][0])

        return tree_list[n][0]

    print(f'#{tc} {int(rec(1))}')