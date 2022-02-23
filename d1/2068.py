T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    max_value = nubmers[0]
    for i in range(len(nubmers)):
        if numbers[i] > max_value:
            max_value = numbers[i]

    print(f'#{tc} {max_value}')
