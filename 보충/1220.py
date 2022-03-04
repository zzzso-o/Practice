T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    for j in range(N):
        temp = []
        for i in range(N):
            if arr[i][j] == 1:
                temp.append(1)
            if arr[i][j] == 2 and temp:
                ans += 1
                temp = []
    print(f'{tc} {ans}')
