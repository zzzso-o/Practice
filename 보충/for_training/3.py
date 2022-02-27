char = ['A', 'T', 'B', 'T', 'S']

N = int(input())
new_list = [0] * 5
if N > 0:
    for i in range(5):
        if i+N > 4:
            new_list[(i+N)-5] = char[i]
        else:
            new_list[i+N] = char[i]
elif N < 0:
    for i in range(5):
        new_list[i+N] = char[i]

print(*new_list[::])

