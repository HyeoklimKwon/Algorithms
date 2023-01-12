# n = 1260
# count = 0 

# coin_types = [500, 100, 50, 10]

# for coin in coin_types:
#     count += n
#     n %= coin

# print(count)

# 이게 정답이라고?? 해당 문제에 대한 정답이 아니라서 다시 올바른 코드로 작성해보자

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    # 몫을 구하고 카운트에 더해줌
    mok = n // coin   
    count += mok
    # 나머지 값을 n으로 설정
    remain =  n % coin      
    n = remain
print(count)
  
