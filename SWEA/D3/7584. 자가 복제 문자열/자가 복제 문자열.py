T = int(input())

def sol():
    k = int(input()) - 1

    while True:
        if k % 2 == 1:
            k //= 2
        if k % 4 == 0:
            return 0
        elif k % 2 == 0:
            return 1

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')