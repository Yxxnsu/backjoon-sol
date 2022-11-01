T = int(input())

def sol():

    m, d = map(int, input().split())
    day = [0,1,2,3,4,5,6]

    diff = 0
    for i in range(1, m):
        if i in (1,3,5,7,8,10,12):
            diff += 31
        elif i == 2:
            diff += 29
        else:
            diff += 30
    diff += d - 1
    day_idx = diff % 7 - 3
    return day[day_idx]
 
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')