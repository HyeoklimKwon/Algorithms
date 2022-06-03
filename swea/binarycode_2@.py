import sys
sys.stdin = open('binarycode2_input.txt')


# 코드 부분만 추출하기
def extract_decimal_code(in_str):
    code = list()   # 10진 암호 코드 하나하나씩 저장할 배열 (8개 채우면 빈 배열로 리셋)
    idx = len(in_str) - 1
    # in_str의 뒤->앞으로 역순으로 조사
    while idx >= 0:
        # 1을 만나면 그 때부터 암호코드 추출 시작
        if in_str[idx] == '1':
            # 0001101 이면
            # n1=3 / n2=2 / n3=1 / n4=1
            n1 = n2 = n3 = n4 = 0
            # n4 추출
            while in_str[idx] == '1':
                n4 += 1
                idx -= 1
            # n3 추출
            while in_str[idx] == '0':
                n3 += 1
                idx -= 1
            # n2 추출
            while in_str[idx] == '1':
                n2 += 1
                idx -= 1
            # n1 추출 (n1이 어디까지인지 알 수 없기 때문에
            # 전체 크기인 (7*multiple)에서 n2 n3 n4를 빼면 -> n1
            #   multiple은 배수 (전체 크기가 7, 14, 21, 28 ... 이기 때문)
            multiple = min(n2, n3, n4)
            n1 = (7 * multiple) - (n2 + n3 + n4)
            # 암호 코드 끝나는 부분으로 idx 옮기기
            idx -= n1
            # 배율 빼주기
            #   6 : 4 : 2 : 2 인 경우 -> 3 : 2 : 1 : 1 로 바꿔줌
            n1 //= multiple
            n2 //= multiple
            n3 //= multiple
            n4 //= multiple
            # 3 : 2 : 1 : 1 -> 십진수로 얻기 (원소의 인덱스가 십진수)
            decimal_num = pattern.index((n1, n2, n3, n4))
            # 새로 얻은 십진수를 앞으로 넣는다 (뒤에서 부터 조사했기 때문)
            code.insert(0, decimal_num)
            # 암호 코드 한 세트를 추출했으면 -> 암호 코드 추가해주고, 코드를 담을 변수는 리셋
            if len(code) == 8:
                if ((code[0] + code[2] + code[4] + code[6]) * 3 + code[1] + code[3] + code[5] + code[7]) % 10 == 0:
                    if code not in decimal_codes:
                        decimal_codes.append(code)
                code = list()
        # 암호와 상관없는 부분은 그냥 패스
        else:
            idx -= 1


# 2진수 코드 비율 -> 10진수
pattern = [
    (3, 2, 1, 1), (2, 2, 2, 1), (2, 1, 2, 2), (1, 4, 1, 1), (1, 1, 3, 2),
    (1, 2, 3, 1), (1, 1, 1, 4), (1, 3, 1, 2), (1, 2, 1, 3), (3, 1, 1, 2)
]

# 16진수 -> 2진수
hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    in_arr = [input() for _ in range(N)]
    in_arr = list(set(in_arr))  # 중복 row 제거

    decimal_codes = list()
    for i in range(len(in_arr)):
        arr = in_arr[i]
        for j in range(M):
            if arr[j] != '0' or arr[len(arr) - i - 1] != '0':
                # 16진 코드 -> 2진 코드 변환
                binary_code = ''
                for k in range(M):
                    binary_code += hex_to_bin[arr[k]]
                binary_code = binary_code.rstrip('0')
                # 2진 코드 -> 10진수 코드 변환 (유효성 검사, 중복 검사 포함)
                extract_decimal_code(binary_code)
                break
    result = 0
    code_length = len(decimal_codes)
    for i in range(code_length):
        result += sum(decimal_codes[i])

    print('#{} {}'.format(tc, result))