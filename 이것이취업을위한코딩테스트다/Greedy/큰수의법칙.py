# n, m , k = map(int, input().split())
# number_list = list(map(int, input().split()))

# first_num = max(number_list)
# number_list.remove(first_num)
# second_num = max(number_list)

# cnt = 1
# result = 0
# for _ in range(m):    
#     if cnt == k :
#         result += second_num
#         cnt = 1
#     else :
#         result += first_num
#         cnt += 1
# print(result)

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

# 크기순으로 정렬 한다음 제일 큰 수 , 그 다음으로 큰 수 저장
data.sort()
first_num = data[n - 1]
second_num = data[n -2]
result = 0

# 반복문 순회하면서 숫자 하나를 더할때마다 m에서 1을 빼줘서 총 m만큼 더하게 하기
while True:
    # 이론상 k 번 제일 큰 수를 더하기
    for i in range(k):
        # 그 전에 m이 0인지 검사 만약 0이면 m번 더했기 때문에 종료
        if m == 0:
            break
        result += first_num
        m -= 1
    if m == 0:
        break
    result += second_num
    m -= 1
print(result)