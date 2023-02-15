def solution(triangle):
    for i in range(len(triangle) - 1 , 0, -1):
        for j in range(len(triangle[i]) - 1):
            if triangle[i][j] >= triangle[i][j + 1]:
                triangle[i - 1][j] += triangle[i][j]
            else :
                triangle[i - 1][j] += triangle[i][j + 1]
    
    answer = triangle[0][0]
    return answer