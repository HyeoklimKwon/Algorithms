import copy
def solution(want, number, discount):
    buylist = {}
    # initiallist = buylist.copy()
    for i in range(len(want)):
        buylist[want[i]] = number[i]
    cnt = 0
    for i in range(len(discount) - 9):        
        for j in range(i, i + 10):
            if buylist.get(discount[j]) :
                buylist[discount[j]] -= 1
                if buylist[discount[j]] == 0 :
                    del buylist[discount[j]]
        # print(buylist)
        if len(buylist) == 0:
            cnt += 1
        for i in range(len(want)):
            buylist[want[i]] = number[i]
        # print(buylist)
            
    answer = cnt
    return answer