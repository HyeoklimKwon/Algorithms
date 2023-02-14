# def solution(topping):
#     cnt = 0
#     init = {}
#     for top in topping:
#         if init.get(str(top)):
#             init[str(top)] += 1
#         else :
#             init[str(top)] = 1
    
#     first_list = [topping[0]]
#     for i in range(len(topping)):
#         if topping[i] not in first_list:
#             first_list.append(topping[i])
#         init[str(topping[i])] -= 1
#         # print(init)
#         if init[str(topping[i])] == 0:
#             del init[str(topping[i])]
#         if len(first_list) == len(init):
#             # print(first_list)
#             # print(init)
#             cnt += 1
    
        
#     answer = cnt
#     return answer
def solution(topping):
    answer = 0
    #length = len(topping)

    forward = set()
    backward = {}
    for i in topping:
        backward[str(i)] = backward.get(str(i), 0)
        backward[str(i)] += 1
    for i in topping:
        forward.add(i)
        backward[str(i)] -= 1
        if backward[str(i)] == 0:
            del backward[str(i)]
        if len(forward) == len(backward.keys()):
            answer += 1
    return answer