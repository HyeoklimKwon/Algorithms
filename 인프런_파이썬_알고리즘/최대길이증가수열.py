n = int(input())
number_list = list(map(int, input().split(" ")))
dy = [0] * (n + 1)
dy[0] = 1

for i in range(2, n):
    tmp = 0
    for j in range(i):        
        if number_list[i] > number_list[j]:
            if tmp < dy[j] + 1:
                tmp = dy[j] + 1
    dy[i] = tmp
print(max(dy))