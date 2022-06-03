import sys
sys.stdin = open('forth.txt')


T = int(input())

for tc in range(1, T+1):
    calc_list = list(input().split())
    stack = []
    result = 'error'
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
            elif calc == '.':
                if len(stack) == 1:
                    result = stack.pop()
                else:
                    result = 'error'
                    break
    print(f'#{tc} {result}')




