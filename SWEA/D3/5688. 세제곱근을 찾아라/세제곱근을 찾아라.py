T = int(input())

def sol():
    
    n = int(input())

    if round(n ** (1/3)) ** 3 == n:
        return round(n ** (1/3))
    else:
        return -1

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')