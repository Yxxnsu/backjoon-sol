T = int(input())

def sol():
    n = int(input())
    li = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    c = [int(input()) for _ in range(p)]
    ans = [0] * p

    for a,b in li:
        for i in range(a, b+1):
            if i in c:
                l = [j for j in range(p) if c[j] == i]
                for j in l:
                    ans[j] += 1
    
    ans = map(str, ans)
    return ' '.join(ans)


for tc in range(1, T+1):
    print(f'#{tc} {sol()}')