```python
import sys
sys.stdin = open('finding_road_input.txt')

for _ in range(1, 11):
    tc, p = map(int, input().split())
    path = list(map(int, input().split()))
    nod_mat = [[] for _ in range(100)]
    #숫자 배열을 받을 2차원 리스트를 만든다
    for i in range(p):
        #들어오는 인덱스 짝수 0 2 4..등은 시작점이고 홀수는 정점이기 때문에 짝수값을 인덱스로 해서 홀수 값을 추가해준다.
        nod_mat[path[2*i]].append(path[2*i+1])
    #while문을 break하기 위해서 flag 사용
    flag = True
    #경로 스택 생성
    visit_list = [0]
    #결과 초기값 설정
    result = 0
    print(nod_mat)
    while flag:
        # visit_list의 가장 마지막 노드에 길이 있을 경우
        if nod_mat[visit_list[-1]]:
            k = nod_mat[visit_list[-1]].pop()
            visit_list.append(k)
            if k == 99:
                result = 1
                flag = False
        # visit_list의 가장 마지막 노드에 길이 없을 경우
        else:
            #불가능한 길이기 때문에 제거 다시 전의 노드로 돌아가서 연산
            visit_list.pop()
            #남아있는 visit_list 요소가 없는 경우 불가능
            if len(visit_list) == 0:
                flag = False
    print(f"#{tc} {result}")
```

