def solution(numbers):
    answer = ''
    numbers.sort(reverse=True, key = lambda x : str(x)*3) # 사전식 정렬 - 파이썬 특징
    numbers=''.join(str(s) for s in numbers)
    return "0" if numbers[0]=="0" else numbers