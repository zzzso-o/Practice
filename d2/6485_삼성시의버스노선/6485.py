T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    bus_stops = []
    for _ in range(P):
        bus_stops.append(int(input()))

    bucket = [0] * 5001
    for i in range(P):
        if bus_stops[i] in arr:
            bucket[i+1] = bus_stops[i]

