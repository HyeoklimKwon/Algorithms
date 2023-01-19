n = int(input())
statues = list(map(int, input().split()))

# result = 1

# def goldpaint(s_list):
#     return abs(s_list.count(1) - s_list.count(2))

# if n == 1:
#     print(result)
# else :
#     # 0 ~  n - 1
#     for i in range(n - 1):
#         print(i)
#         if result >= n - i :
#             break
#         for j in range(i + 1):
#             tmp = goldpaint((statues[j : n - i + j]))
#             if result < tmp :
#                 result = tmp
# print(result)

left_max = 0
right_max = 0
total_max = 0
for i in range(len(statues)):
    if statues[i] == 1:
        left_max += 1
        right_max -= 1
        if right_max < 0 :
            right_max = 0
        tmp_max = max(left_max, right_max)

    else :
        left_max -= 1
        right_max += 1
        if left_max < 0 :
            left_max = 0
        tmp_max = max(left_max, right_max)
    if tmp_max > total_max :
        total_max = tmp_max
print(total_max)




        





