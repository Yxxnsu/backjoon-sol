T = int(input())

def sol():
    n = int(input())

    ans = 0.0
    for _ in range(n):
        p, x = map(float, input().split())
        ans += p * x
    return f'{ans:.6f}'

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')