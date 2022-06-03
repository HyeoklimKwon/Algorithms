```python
#후위 표기법으로 변환해주는 함수
def make_post(expression):
    #스택에 있을경우 우선순위
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    #들어올때 우선순위
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    stack = []
    ans = ""
    for s in expression:
        #숫자일 경우 후위표기법에 추가
        if s.isdigit():
            ans += s
        #닫는 가로가 나오면 열린가로가 나올때까지 모두 pop해서 후위표기법에 추가
        elif s == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        else:
        #스택안의 우선순위가 들어오는 우선순위보다 높을경우 낮을때까지 pop한 후 추가
            while stack and icp[s] <= isp[stack[-1]]:
                ans += stack.pop()
            #그렇지 않을 경우 그냥 스택에 push
            stack.append(s)
    #모든 과정이 끝난후 stack안에 있는 연산자들 후위 표기법에 모두 추가
    while stack:
        ans += stack.pop()
    return ans

T = 10
for tc in range(1, T+1):
    N = int(input())
    temp_list = list(input())
    #입력받은 리스트를 후위표기법으로 변환해주기
    calc_list = make_post(temp_list)
    stack = []
    for calc in calc_list:
        if calc.isdigit():
            stack.append(int(calc))
        else:
            #더하기일 경우
            if calc == '+':
                if len(stack) < 2:
                    break
                else:
                    stack.append(stack.pop()+stack.pop())
            #곱셈일 경우
            elif calc == '*':
                if len(stack) < 2:
                    break
                else:
                    stack.append(stack.pop()*stack.pop())
            #나눗셈일 경우
            elif calc == '/':
                if len(stack) < 2:
                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b//a)
            #뺄셈일 경우
            elif calc == '-':
                if len(stack) < 2:
                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append((b-a))
    print(f'#{tc} {stack[0]}')
```

