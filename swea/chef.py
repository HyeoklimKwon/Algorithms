import sys
sys.stdin = open('chef_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    number_list = []
    for i in range(N):
        number_list.append(i)

    cook_list = [list(map(int, input().split())) for _ in range(N)]
    total_part = []
    for i in range(1 << N):
        part = []
        for j in range(N):
            if i & (1 << j):
                part.append(number_list[j])
        total_part.append(part)
    cook_part = []
    for id in range(len(total_part)):
        if len(total_part[id]) == N//2:
            cook_part.append(total_part[id])
    a_synergy = []
    b_synergy = []
    for idx in range(len(cook_part)//2):
        # pair = [cook_part[idx], cook_part[-(idx+1)]]
        a_sum = 0
        b_sum = 0
        for i in cook_part[idx]:
            for j in cook_part[idx]:
                a_sum += cook_list[i][j]
        a_synergy.append(a_sum)
        for i in cook_part[-(idx+1)]:
            for j in cook_part[-(idx+1)]:
                b_sum += cook_list[i][j]
        b_synergy.append(b_sum)
    subs_list = []
    for l in range(len(cook_part)//2):
        subs_list.append(abs(a_synergy[l]-b_synergy[l]))

    print(f'#{tc} {min(subs_list)}')










