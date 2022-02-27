import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    sol = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for dx in range(M):
                for dy in range(M):
                    total += arr[i+dx][j+dy]
            if sol < total:
                sol = total

    # max_v = total_list[0]
    # for idx in range(len(total_list)):
    #     if total_list[idx] > max_v:
    #         max_v = total_list[idx]

    print(f'#{tc} {sol}')