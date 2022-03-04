import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    max_v = 0
# 행순회
    for i in range(N):
        cnt = 0
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                if j == M-1 and cnt > max_v:
                    max_v = cnt
            else:
                if cnt > max_v:
                    max_v = cnt
                cnt = 0
# 열순회
    for j in range(M):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if i == N-1 and cnt > max_v:
                    max_v = cnt
            else:
                if cnt > max_v:
                    max_v = cnt
                cnt = 0

    print(f'#{tc} {max_v}')