list_a = [9, 3, 5, 7, 4]
N = int(input())
new_list = [0] * 5
for i in range(len(list_a)):
    if i+N > 4:
        new_list[(i+N)-5] = list_a[i]
    else:
        new_list[i+N] = list_a[i]
print(*new_list[::])