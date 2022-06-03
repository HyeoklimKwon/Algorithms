import sys
sys.stdin = open('inorder_input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input()) #노드 개수
    input_list = [list(map(str, input().split())) for _ in range(N)]
    # 해석용 딕셔너리 만들기
    code_dict = dict()
    for i in range(N):
        code_dict[input_list[i][0]] = input_list[i][1]
        input_list[i].pop(1)
    node_list = []
    for i in range(N):
        for j in range(1, len(input_list[i])):
            node_list.append(int(input_list[i][0]))
            node_list.append(int(input_list[i][j]))

    c1 = [0]*(N+1)
    c2 = [0]*(N+1)
    for i in range(len(node_list)//2):
        if not c1[node_list[2*i]]: #0일 경우
            c1[node_list[2*i]] = node_list[2*i+1]
        else: #채워져 있을 경우
            c2[node_list[2*i]] = node_list[2*i+1]

    #중위 순환법으로 순환하는 노드 번호 저장
    number_list = []
    #중위 순환법 함수 생성
    def in_order(v):
        global number_list
        if v:
            in_order(c1[v])
            number_list.append(v)
            in_order(c2[v])

    in_order(1)

    result_list = []
    # 만들어둔 코드 딕셔너리로 노드번호를 문자로 변환 후 출력
    for i in range(len(number_list)):
        result_list.append(code_dict[str(number_list[i])])
    result = "".join(result_list)
    print(f'#{tc} {result}')



