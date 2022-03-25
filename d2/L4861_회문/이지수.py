import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    text = list(input() for _ in range(n))

    result = []
    for i in range(n):
        for j in range(n-m+1):

            if text[i][j+m] == text[i][j+m][::-1]:
                result.append(text[i][j])


    for i in range(n-m+1):
        for j in range(n):
            if text[j][i+m] == text[j][i+m][::-1]:
                result.append(text[j][i+m])