import sys
sys.stdin = open('graph_dest_input.txt')

T = int(input())
for tc in range(1, T+1):
    v, e = list(map(int, input().split()))
    nod_mat = [[0]*(v+1) for _ in range(v+1)]
    # v: 노드의 개수 e : 간선의 개수
    for _ in range(e):
        num1, num2 = list(map(int, input().split()))
        nod_mat[num1][num2] = 1
        nod_mat[num2][num1] = 1
    s, g = list(map(int, input().split()))

    visit_list = [s]
    while True:
        flag = False
        for i in range(v+1):
            if nod_mat[s][i]:
                if i not in visit_list:
                    visit_list.append(i)
                    if i == g:
                        flag = True
                        break
                    s = i
                else:
                    nod_mat[s][i] = 0
                    if sum(nod_mat[s]) == 0:
                        s_index = visit_list.index(s)
                        s = visit_list[s_index-1]
                        if sum(nod_mat[s]) == 0:
                            flag = True

        if flag == True:
            break
        if len(visit_list) == v:
            break
    result = 0
    if g in visit_list:
        result = 1
    print(visit_list)
    print(f'# {tc} {result}')
















