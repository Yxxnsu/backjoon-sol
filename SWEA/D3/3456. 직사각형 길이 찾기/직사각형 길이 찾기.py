T = int(input())

def sol():
    
    a, b, c = map(int, input().split())

    if a == b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a

ans = []
for tc in range(1, T+1):
    ans.append(f'#{tc} {sol()}')
print(*ans, sep='\n')