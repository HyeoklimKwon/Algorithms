N = int(input())
# 탐욕 알고리즘? 가지치기
# 재귀

def hanoi(N, s, o, e):
    if N == 0:
        return
    hanoi(N - 1, s, e, o)
    print(f'{N}: {s} -> {e}')
    hanoi(N - 1, o, s, e)
hanoi(N, 1, 2, 3)



