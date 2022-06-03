import sys
sys.stdin = open('binarycode2_input.txt')

alphabet = {'A': 1010, 'B': 1011, 'C': 1100, 'D': 1101,
                      'E': 1110, 'F': 1111}


def to_b(number):
    bin_num = ''
    for n in number:
        if n.isdigit():
            n = int(n)
            a = []
            while n:
                k = n % 2
                a.append(k)
                n = n // 2
            a.reverse()
            while len(a) != 4:
                a.insert(0, 0)
            result = ''
            for i in range(len(a)):
                result += str(a[i])
            bin_num += result
        else:
            result = alphabet[n]
            bin_num += str(result)
    return bin_num

def get_total(code):
    b_num = to_b(code)
    code_list = b_num
    k = int(7 * (len(b_num) / 56))
    code_arr = []
    for i in range(8):
        num_list = []
        for j in range(k * i, k * (i + 1)):
            num_list.append(code_list[j])
        code_arr.append(num_list)
    prop_list = []
    for i in range(8):
        cnt = 1
        res = ''
        for j in range(len(code_arr[i]) - 1):
            if code_arr[i][j] == code_arr[i][j + 1]:
                cnt += 1
            else:
                cnt = cnt / (len(b_num) / 56)
                res += str(int(cnt))
                cnt = 1
        cnt = cnt / (len(b_num) / 56)
        res += str(int(cnt))
        prop_list.append(res)

    result_list = []
    for i in range(8):
        result_list.append(code_dict[prop_list[i]])

    odd_sum = 0
    even_sum = 0
    last_num = result_list[-1]
    total = sum(result_list)

    for i in range(4):
        odd_sum += result_list[2 * i]
        even_sum += result_list[2 * i + 1]
    even_sum = even_sum - last_num
    check_result = odd_sum * 3 + even_sum + last_num
    if check_result % 10:
        total = 0
    return total



T = int(input())

for tc in range(1):
    N, M = map(int, input().split())
    # arr = [list(map(str, input())) for _ in range(N)]
    arr = sorted(list(set([input()[:M] for _ in range(N)])))
    arr.pop(0)
    code_dict = {'3211': 0, '2221': 1, '2122': 2, '1411': 3, '1132': 4, '1231': 5,
                 '1114': 6, '1312': 7, '1213': 8, '3112': 9}
    final_list = []
    for i in range(len(arr)):
        code = arr[i]
        code = code.strip("0")
        final_list.append(code)
    # for c in final_list:
    #     c = get_total(c)
    code = '68B46DDB9346F4'
    b_num = to_b(code)
    code_list = b_num
    k = int(7 * (len(b_num) / 56))

    # print(get_total('C99624DDAF324C'))
    code_arr = []
    for j in range(0, len(b_num), k):
        num_list = code_list[j:j + k]
        code_arr.append(num_list)
    print(code_list)
    print(code_arr)
    print(to_b('328D1AF6E4C9BB'))




