import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    cnt = 0
    for i in range(99):
        for j in range(100):
            if arr[i][j] == 1:
                if arr[i+1][j] == 2:
                    cnt += 1
                # 0이 나올 경우엔 밑으로 한 칸 이동.
                elif arr[i+1][j] == 0:
                    arr[i+1][j] = arr[i][j]

    print(f'{tc} {cnt}')