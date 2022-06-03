import sys
sys.stdin = open('switch_input.txt')

def change(a):
    if a == 1:
        a = 0
    else:
        a = 1
    return a



N = int(input())
switch_list = list(map(int,input().split()))
k = int(input())
student_list = [list(map(int, input().split())) for _ in range(k)]
for i in range(k):
    # 남학생
    if student_list[i][0] == 1:
        boy_index = student_list[i][1] # 3
        plus = int(boy_index)
        while boy_index <= N:
            switch_list[boy_index-1] = change(switch_list[boy_index-1])
            boy_index += plus

    else:
        change_list = []
        girl_index = student_list[i][1] # 3
        for i in range(N):
            if i <= girl_index-1 < N-i:
                if switch_list[girl_index-1-i] == switch_list[girl_index-1+i]:
                    change_list.append(i)
                else:
                    break
        for l in change_list:
            switch_list[girl_index-1-l] = change(switch_list[girl_index-1-l])
            switch_list[girl_index - 1 + l] = change(switch_list[girl_index - 1 + l])
        switch_list[girl_index-1] = change(switch_list[girl_index-1])

for i in range(N):
    if i % 20 == 0 and i != 0:
        print()
    print(switch_list[i], end=' ')





