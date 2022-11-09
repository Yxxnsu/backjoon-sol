T = int(input())

def sol():

    N = int(input())

    s1 = (N + 1) * N // 2
    s2 = 2 * s1 - N

    return f'{s1} {s2} {s2 + N}'

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')