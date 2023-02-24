# from collections import deque
# def solution(number, k):
#     numbers = list(map(int, number))  
#     digitnum = (len(numbers) - k)
#     # print(digitnum)
#     result = ""
#     q = deque(numbers[0 : k + 1])
#     # print(max(q))
#     cnt = 0
#     while True:
#         max_num = max(q)
#         result += str(max_num)
#         if len(result) >= digitnum:
#             break
#         while True:
#             tmp_check = q.popleft()
#             if tmp_check == max_num:
#                 break
#         cnt += 1
#         q.append(numbers[k + cnt])
#     # print(result)
#     answer = result
#     return answer
def solution(number, k):
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)