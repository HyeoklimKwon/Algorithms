import sys
sys.stdin = open('max_prob_input.txt')

T = int(input())

def max_prob(a, c_prob):
    global max_p
    if a == N:
        if max_p < c_prob:
            max_p = c_prob

    if max_p >= c_prob:
        return

    for i in range(N):
        if worked[i] == 0:
            worked[i] = 1
            max_prob(a + 1, c_prob*percent_list[a][i])
            worked[i] = 0

for tc in range(1, T + 1):
    N = int(input())
    percent_list = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]
    max_p = 0
    worked = [0]*N
    max_prob(0, 1.0)
    max_p = max_p*100
    print('#{} {:.6f}'.format(tc, round(max_p, 6)))

