import sys
sys.stdin = open('calculator2_input.txt')
def make_post(expression):
    isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    stack = []
    ans = ""
    for s in expression:
        if s.isdigit():
            ans += s
        elif s == ')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
        else:
            while stack and icp[s] <= isp[stack[-1]]:
                ans += stack.pop()
            stack.append(s)
    while stack:
        ans += stack.pop()
    return ans

T = 10
for tc in range(1, T+1):
    N = int(input())
    temp_list = list(input())
    calc_list = make_post(temp_list)
    stack = []
    for calc in calc_list:
        if calc.isdigit():
            stack.append(int(calc))
        else:
            if calc == '+':
                if len(stack) < 2:
                    break
                else:
                    stack.append(stack.pop()+stack.pop())
            elif calc == '*':
                if len(stack) < 2:
                    break
                else:
                    stack.append(stack.pop()*stack.pop())
            elif calc == '/':
                if len(stack) < 2:
                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b//a)
            elif calc == '-':
                if len(stack) < 2:
                    break
                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append((b-a))
    print(f'#{tc} {stack[0]}')