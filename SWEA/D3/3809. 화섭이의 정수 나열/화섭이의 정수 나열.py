T = int(input())

def sol():
    N = int(input())
    s = ''
    while len(s) != N:
        s += ''.join(map(str, input().split()))
    for i in range(1000):
        s_i = str(i)
        if s.find(s_i) == -1:
            return i

for tc in range(1, T+1):
    print(f'#{tc} {sol()}')