from datetime import datetime, timedelta
def solution(book_time):
    
    # 1. 문자열 변수들에 시간임 적용
    times = []
    time_form = '%H:%M'
    for i in range(len(book_time)):
        tmp_list = []
        for j in range(2):
            tmp_list.append(datetime.strptime(book_time[i][j], time_form))
        times.append(tmp_list)        
    # 2. 입실 시간 기준으로 제일 빠른 순으로 정렬
    times.sort(key = lambda x:x[0])
    # 3. 들어갈 경우 뒤 시간에 10분 + 적용
    clean_time =  timedelta(minutes = 10)
    now_list = [times[0][1] + clean_time]
    # print(now_list)
    # print("+++=")
    for i in range(1, len(times)):
        for j in range(len(now_list)):
            if times[i][0] >= now_list[j]:
                del now_list[j]                
                break
        now_list.append(times[i][1] + clean_time)
    # print(now_list)
        
            
    # 4. 후에 들어올 시간 리스트의 입실 시간과 들어가 있는 퇴실+ 10분 비교
    # 5. 입실 시간이 적을 경우, 퇴실 시간과 입실 시간비교 있을 경우 , 
    answer = len(now_list)
    return answer