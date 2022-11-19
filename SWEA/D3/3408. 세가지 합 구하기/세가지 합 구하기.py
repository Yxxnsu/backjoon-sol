T = int(input())

def sol():

    N = int(input())

    s1 = ((N+1) * N) // 2
    s2 = s1 + ((N-1) * N) // 2
    s3 = s2 + N

    return f'{s1} {s2} {s3}'
        
for tc in range(1, T+1):
    print(f'#{tc} {sol()}')