import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for i in range(N):
        for j in range(N):
            s = arr[i][j] # 중심값 초기화
            for k in range(4):
                for z in range(1, M):
                    ni, nj = i + di[k]*z, j + dj[k]*z
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]

            if max_v < s:
                max_v = s

            s = arr[i][j]
            dxi = [1, 1, -1, -1]
            dxj = [1, -1, -1, 1]
            for k in range(4):
                for z in range(1, M):
                    ni, nj = i + dxi[k]*z, j + dxj[k]*z
                    if 0 <= ni < N and 0 <= nj < N:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s

    print(f'#{tc} {max_v}')
