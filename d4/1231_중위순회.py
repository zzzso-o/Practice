import sys
sys.stdin = open('input.txt')

def postorder(root):
    if root:
        postorder(Tree[root][0])
        print(root)
        postorder(Tree[root][1])


for tc in range(1, 11):
    N = int(input())
    tree = list(map(str, input().split()))
    Tree = [[0]*3 for _ in range(N+1)]
    # for i in range(0, len(tree), 2):
print(f'{tc} {postorder(tree)}')