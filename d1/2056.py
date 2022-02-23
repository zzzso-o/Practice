# import sys
# sys.stdin = open('input.txt')

mon_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mon_list = [1,2,3,4,5,6,7,8,9,10,11,12]



T = int(input())
for tc in range(1, T+1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:8]

    if int(year) > 0:
        if int(month) in mon_list:
            if int(day) <= mon_day[int(month)-1]:
                print(f'#{tc} {year}/{month}/{day}')
            else:
                print(f'#{tc} -1')
        else:
            print(f'#{tc} -1')