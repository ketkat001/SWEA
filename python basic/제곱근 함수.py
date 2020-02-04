def my_sqrt(n):
    x, y = 1, n
    result = 1

    # 제곱근의 제곱 (result**2) 과 입력 값(n)의 차이가 적어도 이 차이보다 작다면,

    while (abs(n - result**2) > 0.00000001):   # 1e-10
        result = (x + y) / 2
        if result**2 < n:    # 제곱근의 제곱이 입력 값보다 작으면, 앞 범위를 제곱근(result)으로 변경
            x = result

        else:                # 반대로 입력 값보다 크다면 뒷 범위를 제곱근(result)으로 변경
            y = result
    return round(result, 6)
x = int(input())
print(my_sqrt(x))