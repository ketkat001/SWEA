T = int(input())
for i in range(T):
    N = int(input())
    price_list = list(map(int, input().split()))
    max_price = price_list[N - 1]             # max_price 값을 리스트 맨 뒷값으로 선언
    price_list.reverse()                      # price_list를 뒤집어 정렬
    sum = 0
    for price in price_list:
        if price > max_price:                 # price 값이 max_price 값보다 크면 max_price 값을 바꿈
            max_price = price
        sum += max_price - price              # sum에 시세 차이값을 저장
    print(f'#{i + 1} {sum}')