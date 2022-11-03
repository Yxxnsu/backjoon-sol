T = int(input())

def dayToHour():
    pass

def hourToSecond():
    pass

def sol():

    d, h, m = map(int, input().split())    

    if (d == 11 and h < 11) or (d == 11 and h == 11 and m < 11):
        return -1

    diff = d - 11
    
    ans = 0
    if diff > 0:
        ans = (24 * 60 * (diff-1)) + 768 + (h * 60) + m + 1
    else:
        diff_h = h - 11
        if diff_h > 0:
            ans = (60 * (diff_h-1)) + m + 49
        else:
            ans = m - 11
        
    return ans

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')