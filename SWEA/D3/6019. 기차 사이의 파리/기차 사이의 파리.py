T = int(input())

def sol():
    
    d, a, b, f = map(float, input().split())
    t = d / (a + b)
    return f'{t * f:.6f}'
    
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')