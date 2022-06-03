```python
```

```python
for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    total = 0
    for i in range(2, N-2):
        if buildings[i] > buildings[i-2] and buildings[i] > buildings[i-1] and buildings[i] > buildings[i+1] and buildings[i] > buildings[i+2]:
            total += buildings[i] - max([buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]])
    print(f"#{tc} {total}")
    #빌딩문제
    
```