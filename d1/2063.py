import sys
sys.stdin = open('input.txt')

N = int(input())
scores = list(map(int, input().split()))

cnt = [0] * N
for i in range(len(scores), 1, -1):
    for j in range(N-1):
        if scores[j] > scores[j+1]:
            scores[j] = scores[j+1]
            scores[j+1] = scores[j]
    print(cnt[N//2+1])\
