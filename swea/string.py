import sys
sys.stdin = open('string_input.txt')

T = int(input())


for tc in range(1, T+1):
    p = list(input())
    t = list(input())
    i = 0
    j = 0
    while j < len(p) and i < len(t):
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i+1
        j = j+1
    if j == len(p):
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')

