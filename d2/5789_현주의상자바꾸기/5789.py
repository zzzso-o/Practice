import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(Q)]

    boxes = [0] * (N+1)
    for i in range(1, Q+1):
        for idx in range(arr[i-1][0], arr[i-1][1]+1):
            boxes[idx] = i


    print(f'#{tc}', *boxes[1:])