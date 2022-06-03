```python
T = int(input())
#파스칼의 삼각형을 재귀함수의 형태로 만든다.
def pascal(n):
    if n < 2: # 첫번째 줄 [1]부터 시작하면 인덱스에러가 발생할 듯하여 그 다음줄 부터 시작하였다.
        return [1, 1]
    else:
        number_list = [1]*(n+1)
        for i in range(1, n):
            number_list[i] = pascal(n-1)[i] + pascal(n-1)[i-1] #전의 함수 리스트의 같은 인덱스와 전의 인덱스의 합 삽입
        return number_list





for tc in range(1, T+1):
    N = int(input())
    k = 0
    pascal_zero = '1' #처음 줄을 빼고 함수를 만들었기에 추가
    print('#%d' %tc)
    print(pascal_zero)
    for i in range(1,N):
        result = map(str,pascal(i)) #type이 int여서 str으로 바꿔주고 join 메서드로 출력
        print(' '.join(result))
```

