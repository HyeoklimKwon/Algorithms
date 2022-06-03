import sys
sys.stdin = open('calculator_input.txt')


def make_post(expression):
    isp = {'+': 1,  '*': 2}
    icp = {'+': 1,  '*': 2}
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
    calc_list = list(input())
    calc_list = make_post(calc_list)
    stack = []
    for calc in calc_list:
        if calc == "+":
            stack.append(stack.pop() + stack.pop())
        elif calc == "*":
            stack.append(stack.pop()*stack.pop())
        else:
            stack.append(int(calc))
    print(calc_list)
    print(f'# {tc} {stack[0]}')



