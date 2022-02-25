import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    for i in range(9):
        for j in range(8):
            if arr[i][j] == arr[i][j+1]:
                break
        print(f'{tc} {0}')

    for j in range(9):
        for i in range(8):
            if arr[j][i] == arr[j][i+1]:
                break
        print(f'{tc} {0}')

    for _ in range(9):
        for idx in range(1, 8, 3):
            if arr[idx][idx] == arr[idx+1][idx-1] or
