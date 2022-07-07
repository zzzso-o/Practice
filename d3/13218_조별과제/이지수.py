import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    ans = N//3
    print(f'#{tc} {ans}')