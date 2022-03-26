import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    text = list(input() for _ in range(n))

    result = []
    for i in range(n):
        for j in range(n-m+1):
            if text[i][j:j+m] == text[i][j:j+m][::-1]:
                result.append(text[i][j:j+m])


    for i in range(n-m+1):
        for j in range(n):
            c_list = []
            for k in range(m):
                c_list.append(text[i+k][j])
            if c_list[::] == c_list[::-1]:
                result.append(''.join(c_list))

    print('#{} {}'.format(tc, result[0]))
