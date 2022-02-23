import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    all_sum = []

    # row의 합
    for i in range(100):
        total1 = 0
        for j in range(100):
            total1 += arr[i][j]
        all_sum.append(total1)

    # col의 합
    for i in range(100):
        total2 = 0
        for j in range(100):
            total2 += arr[j][i]
        all_sum.append(total2)

    # 대각선의 합
    total3 = 0
    for i in range(100):
        total3 += arr[i][99-i]
    all_sum.append(total3)

    total4 = 0
    for i in range(100):
        total4 += arr[i][i]
    all_sum.append(total4)

    print(f'#{tc} {max(all_sum)}')