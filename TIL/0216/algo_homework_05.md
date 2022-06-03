```python
T = int(input())
#해당되는 값들을 딕셔너리로 만들어준다.
num_dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
reverse_num_dict = dict(map(reversed, num_dict.items()))
print(reverse_num_dict)

for _ in range(1, T+1):
    tc, N = list(map(str, input().split()))
    N = int(N)
    #해당 값들을 딕셔너리로 이용해 숫자로 변환
    number_list = list(map(str, input().split()))
    for i in range(N):
        number_list[i] = num_dict[number_list[i]]
    number_list.sort()
	#정렬 후 다시 이 숫자들을 str로 변환
    for k in range(N):
        number_list[k] = reverse_num_dict[number_list[k]]
    print(f'{tc}')
    print(' '.join(number_list))
```

