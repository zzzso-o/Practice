import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split()))

    max_value, min_value = ai[0], ai[0]
    for i in range(N):
        if ai[i] > max_value:
            max_value = ai[i]
        elif ai[i] < min_value:
            min_value = ai[i]
    print(f'#{tc} {max_value - min_value}')