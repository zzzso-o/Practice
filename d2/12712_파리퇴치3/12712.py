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
            s = a[i][j] # 중심값 초기화
            for k in range(4):
                for z in range(1, M):
