def permutation(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    return_array = []
    def generate(chosen, used):
        # 내가 원하는 만큼 뽑았으면, return
        if len(chosen) == r:
            #이 부분에서 append로 고치면 빈 리스트가 추가됨
            return_array.extend(chosen)
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
    result = []
    for i in range(len(return_array)//r):
        result.append(return_array[i*r:i*r + r])
    return result
print(permutation([1,2,3,4], 4))

