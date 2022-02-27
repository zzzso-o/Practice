import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))

    cnt = [0] * 10
    for i in range(10):
        for j in range(N):
            if cards[j] == i:
                cnt[i] += 1

    max_v = cnt[0]
    max_num = 0
    for idx in range(10):
        if cnt[idx] > max_v:
            max_v = cnt[idx]
            max_num = idx
        elif cnt[idx] == max_v:
            if idx > max_num:
                max_num = idx

    print(f'{tc} {max_num} {max_v}')



