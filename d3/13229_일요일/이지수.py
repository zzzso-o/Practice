import sys
sys.stdin = open('input.txt')

T = int(input())
ans = 0
weeks = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for tc in range(1, T+1):
    S = input()
    ans = 7 - weeks.index(S)

    print(f'#{tc} {ans}')