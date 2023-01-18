def solution(word):
    alpha_list = ['A', 'E', 'I', 'O', 'U']
    result = 1
    print(word)
    for i in range(len(word)):
        word_index = alpha_list.index(word[i])
        # print(5 - i)
        left_len = len(alpha_list[0:word_index])
        # print(left_len)
        # print("+++++")
        if left_len :
            for k in range(5 - i):
                result += left_len*5**k 
            result += 1
        else :
            result += 1
       
    answer = result - 1
    return answer