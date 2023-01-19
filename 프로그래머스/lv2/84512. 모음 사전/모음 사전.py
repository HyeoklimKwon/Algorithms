def solution(word):
#     alpha_list = ['A', 'E', 'I', 'O', 'U']
#     result = 1
#     print(word)
#     for i in range(len(word)):
#         word_index = alpha_list.index(word[i])
#         # print(5 - i)
#         left_len = len(alpha_list[0:word_index])
#         # print(left_len)
#         # print("+++++")
#         if left_len :
#             for k in range(5 - i):
#                 result += left_len*5**k 
#             result += 1
#         else :
#             result += 1
       
#     answer = result - 1
    print(word)
    alphabets = ['A', 'E', 'I', 'O', 'U']
    global cnt 
    cnt = 0
    global flag
    flag = False
    
    def dfs(result):
        # print(result)
        global cnt 
        cnt += 1        
        #찾았을떄 True를 반환
        if result == word:
            print("found!")
            return True
        # 못찾았을 경우
        else :
            if len(result) >= 5 :
                return False
            else :
                for alphabet in alphabets:
                    if dfs(result + alphabet):
                        return True
            
    for alphabet in alphabets:
        if dfs(alphabet):
             break
   
            
    answer = cnt
    return answer