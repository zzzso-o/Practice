list_a = [3, 4, 1, 1, 2]

n = int(input())
new_list = [0] * 5
for i in range(0, len(list_a)-1):
    new_list[i+1] = list_a[i]
    new_list[0] = list_a[4]
print(*new_list[::])
