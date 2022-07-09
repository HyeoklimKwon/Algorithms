input_list = list(input().split(' '))
N = input_list[0]
M = input_list[1]
N = int(N)
M = int(M)
dice_list = [0]*N
list_for_2 = []
def rolling_dice(n, m, dice_list):
    global list_for_2
    if n == 0 :
        if m == 2:
            dice_list = sorted(dice_list)
            if dice_list not in list_for_2:
                list_for_2.append(dice_list)
                dice_list = map(str, dice_list)
                dice_list = ' '.join(dice_list)
                print(dice_list)
                return
            else:
                return
        else:
            dice_list = map(str, dice_list)
            dice_list = ' '.join(dice_list)
            print(dice_list)
            return
    #전체 경우의 수 출력
    if m == 1 or m == 2:
        for i in range(1,7):
            dice_list[-n] = i
            rolling_dice(n-1, m, dice_list)
            dice_list[-n] = 0


    # 모두 다 다른 수
    if m == 3:
        for i in range(1,7):
            if i not in dice_list:
                dice_list[-n] = i
                rolling_dice(n-1, m, dice_list)
                dice_list[-n] = 0





rolling_dice(N, M, dice_list)



