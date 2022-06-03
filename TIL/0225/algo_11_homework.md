```python
import sys
sys.stdin = open('make_code_input.txt')

T = 10
for _ in range(1, T+1):
    tc = int(input())
    number_list = list(map(int,input().split()))
    flag = True
    while flag:
        #한 사이클이 5회니까 range를 정해준다.
        for i in range(1, 6):
            #맨앞의 숫자를 가져오고 i를 빼준다음 저장
            tmp = number_list.pop(0) - i
            #만약에 0보다 작을 경우 0으로 저장후 탈출후 while문 정지
            if tmp <= 0:
                tmp = 0
                number_list.append(tmp)
                flag = False
                break
            #아닐 경우는 추가
            number_list.append(tmp)
    #print형식에 맞추기 위해서 사용
    number_list = list(map(str, number_list))
    result = ' '.join(number_list)
    print(f'#{tc} {result}')
```

