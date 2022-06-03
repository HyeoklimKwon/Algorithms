import sys
sys.stdin = open('binary_research_input.txt')

def binary_research(l, r, target):
    c = int((l+r)/2)
    cnt = 0
    while c != target:
        c = int((l+r)/2)
        if c < target:
            l = c
            r = r
        else :
            l = l
            r = c
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T+1):
    l = 1
    result = 0
    r, a_target, b_target = list(map(int, input().split()))
    if binary_research(l,r,a_target) < binary_research(l,r,b_target):
        result = 'A'
    elif binary_research(l,r,a_target) > binary_research(l,r,b_target):
        result = 'B'
    print(f'#{tc} {result}')

