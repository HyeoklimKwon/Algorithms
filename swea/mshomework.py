import sys
sys.stdin = open('mshomework_input.txt')

T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    num_set = set(map(int, input().split()))
    total_set = set()
    for i in range(1, n+1):
        total_set.add(i)
    result_set = total_set - num_set
    result = list(map(str, result_set))
    result = " ".join(result)
    print(f'#{tc} {result}')


