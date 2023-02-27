n = int(input())
tree_list = [list(map(int, input().split(' '))) for _ in range(n - 1)]

# print(n)
print(tree_list)

# node_len = tree_list[-1][1]
# node_matrix = [[0] * (node_len + 1) for _ in range(node_len + 1)]
# for i in range(len(tree_list)):
#     node_matrix[tree_list[i][0]][tree_list[i][1]] = tree_list[i][2]
# 어차피 위에서 아래로 내려가니까 노상관이다.

# 핵심은 왼쪽과 오른쪽을 따로 구해야한다 ? x
# 종점 노드끼리 dfs 한다
# tree_list 마지막 요소에서 마지막 부모와 마지막 자식 노드 즉 마지막 부토 + 1 ~ 마지막 자식은 다 종점 노드라는 거지
last_parent , last_children = tree_list[-1]

not_visited = []
for i in range(last_parent + 1 , last_children + 1):
    not_visited.append[i]

#dfs를 만들고
max_cnt = 0
while not_visited:
    sx = not_visited.pop()
    # tmp_cnt = dfs(sx)
    tmp_cnt = 0
    if tmp_cnt > max_cnt :
        max_cnt = tmp_cnt
    

    


    



    

