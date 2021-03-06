def bin_num(x):               # 2진수를 10진수로 변환
    sum = 0
    bin_list = [128, 64, 32, 16, 8, 4, 2, 1]
    for i in range(0, 8):
        sum += int(x[i]) * bin_list[i]


    return sum

print(bin_num('01001100')) # 순차적으로 2 곱셈
[76, 105, 102, 101, 32, 105, 116, 115, 101, 108, 102, 32, 105, 115, 32, 97, 32, 113, 117, 111, 116, 97, 116, 105, 111, 110, 46]