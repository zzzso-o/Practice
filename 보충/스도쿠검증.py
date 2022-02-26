import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    for i in range(8):
        for j in range(8):
            if arr[i][j] == arr[i][j+1]:
                break
                print(f'{tc} {0}')
            elif arr[j][i] == arr[j][i+1]:
                break
                print(f'{tc} {0}')
