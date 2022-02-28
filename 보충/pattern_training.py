map = [["A","B","G","K"],["T","T","A","B"],["A","C","C","D"]]
pattern = [['A', 'B'], ['C', 'D']]


def is_pattern(y, x):
    for i in range(2):
        for j in range(2):
            if pattern[i][j] != map[i+y][j+x]:
                return 0
    return 1

result = 0
for i in range(2):
    for j in range(3):
        if is_pattern(i, j):
            result += 1

if result != 0:
    print(f'발견 {result}개')
else:
    print('미발견')