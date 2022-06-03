## Q.1 min max

```python
import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    min_V = numbers[0]
    max_V = numbers[0]
    for idx in range(N):
        if min_V > numbers[idx]:
            min_V = numbers[idx]
        if max_V < numbers[idx]:
            max_V = numbers[idx]
    result = max_V - min_V
    print(f'#{tc} {result}')
```



## 	Q.2 구간합 (bubble-sort)

```python
import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1, T+1):
    topic_list = list(map(int, input().split()))
    N = topic_list[0]
    M = topic_list[1]
    numbers = list(map(int, input().split())) 
    total_list = []
    for idx in range(N-M+1):
        total_list.append(sum(numbers[idx:idx+M]))

    total_len = len(total_list)
    for total_idx in range(total_len-1, 0, -1):
        for i in range(total_idx):
            if total_list[i] > total_list[i+1]:
                total_list[i+1] = total_list[i]
                total_list[i] = total_list[i+1]
                
    result = total_list[-1] - total_list[0]
    print(f'#{tc} {result}')
```



## Q.2 구간합 (counting sort)

```python
import sys
sys.stdin = open('sample_input.txt')
#꼭 sort를 사용할 필요는 없다.

T = int(input())

for tc in range(1, T+1):
    topic_list = list(map(int, input().split()))
    N = topic_list[0]
    M = topic_list[1]
    numbers = list(map(int, input().split())) # 1 2 3 4 5 6 7 8 9 10

    Max_num = 100000

    total_list = []
    for idx in range(N-M+1):
        total_list.append(sum(numbers[idx:idx+M]))

    total_len = len(total_list)

    counting_list = [0]*(Max_num+1)
    counting_sum_list = [0]*(Max_num+1)
    for total in total_list:
        counting_list[total] += 1
    for idx in range(1, len(counting_list)):
        counting_sum_list[idx] = counting_sum_list[idx-1] + counting_list[idx]


    sort_list = [0]*(total_len)
    for total in total_list:
        sort_list[counting_sum_list[total-1]] = total
        counting_sum_list[total] -= 1


    result = sort_list[-1]-sort_list[0]
    print(f'#{tc} {result}')

```





## Q.3  전기버스

```python
import sys
sys.stdin = open('electric_bus.txt')

T = int(input())

for tc in range(1, T+1):

    K, N, M = map(int, input().split())
    bus_stop_list = list(map(int, input().split()))

    #총 버스 정류장 : range(N+1)

    distance_list = [bus_stop_list[0]]
    max_distance = 0
    distance = 0
    count = 0

    #정류장 간의 거리
    for i in range(M-1):
        distance = bus_stop_list[i+1] - bus_stop_list[i]
        distance_list.append(distance)
    distance_list.append(N-bus_stop_list[-1])

    # 정류장 거리 최댓값
    for distance in distance_list:
        if max_distance < distance:
            max_distance = distance

    bus_fill = int(K)
    # 불가능한 경우 검사
    if max_distance > K:
        print(f'#{tc} {count}')
    else:
        bus_stop_list.append(N)
        for idx in range(len(bus_stop_list)):
            if K < bus_stop_list[idx]:

                K = bus_fill + bus_stop_list[idx-1]
                count += 1
        print(f'#{tc} {count}')
```



## Q.4 카드게임

```python
import sys
sys.stdin = open('number_card.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = input()
    count = [0]*10
    for i in range(N):
        count[int(cards[i])] += 1
    max_value = 0
    max_number = 0
    print(count)
    for idx in range(10):
        if max_value <= count[idx]:
            max_value = count[idx]
            max_number = idx
    print(f'#{tc} {max_number} {max_value}')
```



## Q.5 Flatten

```python
import sys
sys.stdin = open('algo_homework_02_input.txt')
T = 10
# 총 테스트 케이스 10개
for tc in range(1, T+1):
    # 반복문 작성
    count = int(input())
    # 최댓값 +1 최솟값 -1 을 count 만큼 반복하기
    box = list(map(int, input().split()))
    # 박스 리스트 생성
    n = 0
    # 몇번 할지 값 초기화
    while n < count +1: # count 만큼 반복
        for i in range(99):
            if box[i + 1] <= box[i]:
                box[i], box[i + 1] = box[i + 1], box[i]
                #최댓값 맨뒤로 보내기
        for j in range(98):
            if box[j + 1] >= box[j]:
                box[j], box[j + 1] = box[j + 1], box[j]
                #최솟값 그 다음으로 보내기
        max_value = box[-1]
        min_value = box[-2]
        box[-1] -= 1
        box[-2] += 1
        n += 1
    print(f'#{tc} {max_value - min_value}')
```

