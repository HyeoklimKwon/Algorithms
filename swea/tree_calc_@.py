import sys
sys.stdin = open('tree_calc_input.txt')

def pos_order(node):
    x = int(tree[node][0])
    y = int(tree[node][2])
    if tree[node][1] == '+':
        tree[node][1] = pos_order(x) + pos_order(y)
    elif tree[node][1] == '-':
        tree[node][1] = pos_order(x) - pos_order(y)
    elif tree[node][1] == '/':
        tree[node][1] = pos_order(x) / pos_order(y)
    elif tree[node][1] == '*':
        tree[node][1] = pos_order(x) * pos_order(y)
    else:
        tree[node][1] = int(tree[node][1])
    return tree[node][1]

# 완전이진트리가 아님.... => ??
T = 10
for tc in range(1, T + 1):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N + 1)]
    for _ in range(N):
        data = input().split()
        # 노드 벨류가 연산자면
        if data[1] in ["+", "-", "*", "/"]:
            nod, val, lef, rig = int(data[0]), data[1], int(data[2]), int(data[3])
            tree[nod] = [lef, val, rig]

        # 노드 벨류가 정수면
        else:
            nod, val = int(data[0]), int(data[1])
            tree[nod][1] = val

    print(int(pos_order(1)))