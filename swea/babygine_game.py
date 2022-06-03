import sys
sys.stdin = open('babygine_game_input.txt')

T = int(input())


def run(c_list):
    result = 0
    c_set = set(c_list)
    check_list = []
    for i in c_set:
        check_list.append(i)
    check_list.sort()
    cnt = 0
    for i in range(len(check_list)-1):
        if (check_list[i+1] - check_list[i]) == 1:
            cnt += 1
            if cnt == 2:
                result = 1
                break
        else:
            cnt = 0
    return result

def triplet(c_list):
    c_list.sort()
    result = 0
    cnt = 0
    for i in range(len(c_list) - 1):
        if (c_list[i + 1] - c_list[i]) == 0:
            cnt += 1
            if cnt == 2:
                result = 1
                break
        else:
            cnt = 0
    return result


for tc in range(1, T + 1):
    card_list = list(map(int, input().split()))
    player_1 = []
    player_2 = []
    result = 0
    for i in range(len(card_list)//2):
        player_1.append(card_list[2*i])
        if len(player_1) >= 3:
            if run(player_1) or triplet(player_1):
                result = 1
                break
        player_2.append(card_list[2*i+1])
        if len(player_2) >= 3:
            if run(player_2) or triplet(player_2):
                result = 2
                break


    print(f'#{tc} {result}')



