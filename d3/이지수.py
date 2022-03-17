import sys, math
sys.stdin = open('input.txt')
#
# def get_ans(n):
#     x = n ** (1/3)
#     if x == int(x):
#         return int(x)
#     else:
#         return -1

# 세제곱근 x를 구하는 함수
def get_ans(n):
    x = n ** (1/3)
    # 실수 연산 과정에서 오류가 발생하기 때문에 isclose로 비교
    # 64 ** (1/3) => 3.99999999999999999999996 (?) => 반올림해서 return
    if math.isclose(x, round(x)) == True:
        return round(x)
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(f'#{tc} {get_ans(N)}')

