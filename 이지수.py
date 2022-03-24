import sys
sys.stdin = open('input.txt')

def search(di, dj, dir, path):
    global max_eat

    if dir < 2:
        if 0 <= di+x[dir] < N and 0 <= dj + y[dir] < N:
            if road[di+x[dir]][dj+y[dir]] not in path:
                search(di+x[dir], dj+y[dir], dir, path+[road[di+x[dir]][dj+y[dir]]])
            else:
                search(di, dj, dir + 1, path)
        search(di, dj, dir+1, path)
    elif dir == 2:
        if 0 <= di+x[dir] < N and 0<= dj+y[dir] < N:
            if road[di+x[dir]][dj+y[dir]] not in path:
                if di+x[dir]-start[0] == dj+y[dir]-start[1]:
                    search(di+x[dir], dj+y[dir], dir+1, path+[road[di+x[dir]][dj+y[dir]]])
                else:
                    search(di + x[dir], dj + y[dir], dir, path+[road[di+x[dir]][dj+y[dir]]])
            else:
                return
        else:
            return
    else:
        if di+x[dir] != start[0]:
            if road[di+x[dir]][dj+y[dir]] not in path:
                search(di+x[dir], dj+y[dir], dir, path+[road[di+x[dir]][dj+y[dir]]])
            else:
                return
        else:
            if len(path) != 1:
                if len(path) > max_eat:
                    max_eat = len(path)
    return

x = [1, 1, -1, -1]
y = [-1, 1, 1, -1]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]
    max_eat = -1
    for i in range(N-1):
        for j in range(1, N-1):
            start = [i, j]
            search(i, j, 0, [road[i][j]])
    print('#{} {}'.format(tc, max_eat))
