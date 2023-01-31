def solution(msg):
    first_list =  list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    first_list.insert(0,0)
    result = []
    i = 0
    #어차피 마지막은 first_list에서 가지고 오면 됨
    while i < len(msg):       
        tmp_msg = msg[i]
        # K A K       
        while tmp_msg in first_list: 
            i += 1
            if i < len(msg):                            
                # 1 2 3 4
                tmp_msg += msg[i]
            # 뒤에서 두번째 인덱스를 넘을 경우 break
            else :
                break
                # KA AK KA KAO  
        #나온 경우 새롭게 저장해야하는 메세지
        first_list.append(tmp_msg)  
        # print(tmp_msg)
        # print("==")
        # K A   KA        
        # i -= 1
        # # 0  1 3 
        # print(i)
        if i == len(msg):
            if tmp_msg in first_list:
                result.append(first_list.index(tmp_msg)) 
            else :
                if len(tmp_msg) > 1:
                    result.append(first_list.index(tmp_msg[0: -1]))
                else :
                    result.append(first_list.index(tmp_msg))
        else : 
            if len(tmp_msg)> 1:
                result.append(first_list.index(tmp_msg[0: -1])) 
            else :
                result.append(first_list.index(tmp_msg))
        # i += 1
    print(result)    
    # print(test[0:-1])
    answer = result
    return answer