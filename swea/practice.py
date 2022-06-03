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

                K = K + bus_stop_list[idx-1]
                count += 1
        print(f'#{tc} {count}')











