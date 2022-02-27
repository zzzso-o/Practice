import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N-1):
            if arr[i][j] == 'o' and arr[i][j+1] == 'o':
                cnt += 1
                if cnt >= 5:
                    print('YES')
            else:
                cnt = 0


    for i in range(N):
        for j in range(N):
            total = 0
            