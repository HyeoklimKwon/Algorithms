n = int(input())
numbers = list(map(int, input().split()))

tmp_max = numbers[0]
total_max = numbers[0]
for i in range(1, n):
   tmp_max = max(numbers[i], numbers[i] + tmp_max )
   if tmp_max > total_max :
    total_max = tmp_max
print(total_max)