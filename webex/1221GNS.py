import sys
sys.stdin = open('input.txt')

GNS = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())
"""
def char_to_num(word):
    return GNS.index(word)

def num_to_char(num):
    return GNS[num]
"""

for tc in range(1, T+1):
    _, _ = input().split()
    words = input().split()
    numbers = list(map(lambda word: GNS.index(word), words))
    numbers.sort()

    print(f'#{tc}')
    print(' '.join(list(map(lambda num: GNS[num], numbers))))


"""
for tc in range(1, T+1):
 _, _ = input().split()
 words = input().split()
 numbers = []

 for word in words:
     # idx로 검색하기
     # for idx in range(10):
     #     if GNS[idx] == word:
     #         numbers.append(idx)
     #         break
     
     # 
     numbers.append(GNS.index(word))
 numbers.sort()
 
 print(f'#{tc}')    
 for number in numbers:
     print(GNS[number], end=' ')       
 """






