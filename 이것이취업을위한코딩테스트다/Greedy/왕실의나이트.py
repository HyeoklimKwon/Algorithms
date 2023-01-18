input_data = input()
row_num = int(input_data[1])
col_num = int(ord(input_data[0]) - ord('a')) + 1
# ord(문자)
# 하나의 문자를 인자로 받고 해당 문자에 해당하는 유니코드 정수를 반환합니다.
# ord('a')를 넣으면 정수 97을 반환합니다.
# print(row_num, col_num)
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2),]

result = 0
for step in steps:
    dr, dc = step
    row_num += dr
    col_num += dc
    if 0 < row_num <= 8 and 0 < col_num <= 8:
        result += 1
print(result)
