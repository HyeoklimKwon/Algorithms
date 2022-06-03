import sys
sys.stdin = open('golf_input.txt')


def dfs_permutation(array, r):
    i_array = [(x, i) for i, x in enumerate(array)]
    stack = [[i] for _, i in i_array]
    return_list = []

    while len(stack) > 0:
        current = stack.pop()
        for i in range(len(i_array)):
            if i not in current:
                temp = current + [i_array[i][1]]
                if len(temp) == r:
                    elements = []
                    for idx in temp:
                        elements.append(i_array[idx][0])
                    return_list.extend([elements])
                else:
                    stack.append(temp)

    return return_list

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    field = [list(map(int, input().split())) for _ in range(N)]
    input_list = []
    for i in range(1, N):
        input_list.append(i)
    perm_list = dfs_permutation(input_list, N-1)
    total_list = []
    for i in range(len(perm_list)):
        perm_list[i].append(0)
        perm_list[i].insert(0, 0)
        total = 0
        for j in range(len(perm_list[i])-1):
            total += field[perm_list[i][j]][perm_list[i][j + 1]]
        total_list.append(total)
    print(f'#{tc} {min(total_list)}')












