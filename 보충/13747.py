T = int(input())

for tc in range(1, T+1):
    n = int(input())
    price = list(map(int, input().split()))

    max = price[-1] # 801
    profit = 0
    for i in range(n-2, -1, -1):
    # 현재가가 최고가보다 크다면 최고가 갱신
        if price[i] >= max:
            max = price[i]
            # 현재가가 최고가보다 작다면
            # 최고가 - 현재가 이익 누적시키기
        else:
            profit += max - price[i]

    print("#{0} {1}".format(tc, profit))

