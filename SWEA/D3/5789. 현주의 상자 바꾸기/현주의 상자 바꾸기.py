T = int(input())

def sol():

    n, q = map(int, input().split())
    box = [0] * (n+1)

    for i in range(1,q+1):
        l, r = map(int, input().split())
        for j in range(l, r+1):
            box[j] = i
    box = list(map(str, box))
    return ' '.join(box[1:])

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')