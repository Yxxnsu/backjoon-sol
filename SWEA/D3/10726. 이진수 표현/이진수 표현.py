T = int(input())

def sol():
    n, m = map(int,input().split())
    if m == 0:
        return 'OFF'
    for i in range(n):
        if m % 2 == 0:
            return 'OFF'
        else:
            m //= 2
    return 'ON'

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')