import sys
sys.stdin = open('input.txt')

def get_tree(string, N, tree):
    for i in range(0, len(string), 2):
        p = string[i*2]
        c = string[i*2+1]
        if tree[p][0]:
            tree[p][1] = c
        else:
            tree[p][0] = c
        tree[c][0] = p
    return tree

def in_order(node):
    if node != 0:
        left, right = tree[node][1], tree[node][2]

        in_order(left)
        print(node, end=' ')
        in_order(right)

for t in range(1, 11):
    N = int(input())
    tree = [[0, 0, 0] for _ in range(N + 1)]
    iStr = list(map(str, input().split()))
    get_tree(iStr)
    print(f'{t} {in_order(iStr[0][0])}')

