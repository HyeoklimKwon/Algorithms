# def solution(weights):
#     ratio_list = [1, 2, 1/2, 3/2, 2/3, 4/3, 3/4]
#     answer = 0
#     while len(weights) > 1 :
#         now_num = weights.pop()
#         for ratio in ratio_list:
#             answer += weights.count(ratio*now_num)            
#     return answer
from collections import defaultdict

def solution(weights):
    answer = 0
    info = defaultdict(int)
    for w in weights:
        # print(info[w],info[w*2] )
        answer += info[w] + info[w*2] + info[w/2] + info[(w*2)/3] + info[(w*3)/2] + info[(w*4)/3] + info[(w*3)/4]
        # print(answer)
        info[w] += 1
        # print(info)
    return answer