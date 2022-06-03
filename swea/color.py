import sys
sys.stdin = open('color_input.txt')

def width(x1,y1,x2,y2,a1,b1,a2,b2):
     wid = ((min(x2, a2) - max(x1, a1))+1) * ((min(y2, b2) - max(y1, b1))+1) # x2 x1  y2 y1
     if wid < 0:
         return 0
     else:
        return wid


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    colors_list = []
    add_number = 0
    subs_number = 0
    red_list = []
    blue_list = []
    for c in range(N):
        color_list = list(map(int, input().split()))
        colors_list.append(color_list)
        if colors_list[-1] == 1:
            red_list.append(color_list)
        else:
            blue_list.append(color_list)

    for i in range(N-1):
        for j in range(i+1, N):
            if colors_list[i][-1] == colors_list[j][-1]:
                #3개가 겹치는 경우
                if(width(colors_list[i][0], colors_list[i][1], colors_list[i][2], colors_list[i][3], colors_list[j][0], colors_list[j][1], colors_list[j][2], colors_list[j][3])) > 0:
                    if colors_list[i][-1] == 1:
                        for k in range(len(blue_list)):
                            subs_number += width(
                                max(colors_list[i][0], colors_list[j][0]), max(colors_list[i][1], colors_list[j][1]), min(colors_list[i][2], colors_list[j][2]), min(colors_list[i][3], colors_list[j][3]) ,blue_list[k][0] ,blue_list[k][1] ,blue_list[k][2] ,blue_list[k][3])
            else:
                add_number += width(colors_list[i][0], colors_list[i][1], colors_list[i][2], colors_list[i][3], colors_list[j][0], colors_list[j][1], colors_list[j][2], colors_list[j][3])
        result = add_number - subs_number
    print(f'#{tc} {result}')