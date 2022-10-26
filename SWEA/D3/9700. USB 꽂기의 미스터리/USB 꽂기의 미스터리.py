T = int(input())
 
def sol():

    p, q = map(float, input().split())

    if (1-p) * q < p * (1-q) * q:
        return 'YES'
    return 'NO'
    
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')