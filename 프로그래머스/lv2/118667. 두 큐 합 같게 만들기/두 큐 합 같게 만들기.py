def solution(queue1, queue2):
    lst = list(queue1 + queue2)
    length = len(queue1) * 2
    i1 = 0
    i2 = length // 2
    target, flag = divmod(sum(lst), 2)
    if flag:
        return -1
    answer = 0
    sum1 = sum(queue1)
    while i1 >= 0 and i2 < length and i1 < i2:
        if sum1 == target:
            return answer
        elif sum1 < target:
            sum1 += lst[i2]
            i2 += 1
            answer += 1
        else:
            sum1 -= lst[i1]
            i1 += 1
            answer += 1
    return -1