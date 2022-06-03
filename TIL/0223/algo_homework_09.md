```python
#후위 표기법으로 변환해주는 함수 만들기 
def make_post(expression):
    # 우선순위 딕셔너리를 생성해줘서 키값을 불러서 비교
    isp = {'+': 1,  '*': 2 }
    icp = {'+': 1,  '*': 2 }
    stack = []
    ans = ""
    for s in expression:
        #숫자일 경우 추가
        if s.isdigit():
            ans += s
        else:
            #우선순위가 아래일 경우 작지 않을때까지 pop후 ans에 추가
            while stack and icp[s] <= isp[stack[-1]]:
                ans += stack.pop()
            #우선순위가 위일 경우 그냥 push
            stack.append(s)
    #과정이 끝난후 이어붙이기
    while stack:
        ans += stack.pop()
    return ans

T = 10
for tc in range(1, T+1):
    N = int(input())
    calc_list = list(input())
    calc_list = make_post(calc_list)
    stack = []
    
    for calc in calc_list:
        #더하기일 경우 두개를 pop해서 더해준후 다시 stack에 저장
        if calc == "+":
            stack.append(stack.pop() + stack.pop())
        elif calc == "*":
            stack.append(stack.pop()*stack.pop())
        else:
            stack.append(int(calc))
    
    print(f'# {tc} {stack[0]}')

```

